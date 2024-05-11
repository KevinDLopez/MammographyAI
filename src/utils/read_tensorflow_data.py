import tensorflow as tf
from typing import List, Tuple, TypedDict
import numpy as np

data_type = TypedDict("data_type", {"label": List[np.number], "data": List[tf.Tensor]})


def read_tf_data(file: str, storing_dict: data_type):
    def parse_function(example_proto):
        return tf.io.parse_single_example(
            example_proto,
            {
                "label": tf.io.FixedLenFeature([], tf.int64),
                "label_normal": tf.io.FixedLenFeature([], tf.int64),
                "image": tf.io.FixedLenFeature([], tf.string),
            },
        )

    # Extract the data
    with tf.device("/CPU:0"):  # else is filled with GPU memory
        raw_data = tf.data.TFRecordDataset([file])
        parsed_dataset = raw_data.map(parse_function)

    for element in parsed_dataset:
        with tf.device("/CPU:0"):  # else is filled with GPU memory
            image = tf.io.decode_raw(
                element["image"], tf.uint8
            )  # shape = (89401,0) - 299*299 = 89401
            image = tf.reshape(image, [299, 299, 1])  # gray scale image
            label = np.int8(element["label_normal"].numpy())
            storing_dict["label"].append(label)
            storing_dict["data"].append(image)


# allocating the data to the memory, with a small batch size. Previously the training was not happening.
def create_tf_dataset(data_dict, batch_size):
    def generator(data, labels):
        for d, l in zip(data, labels):
            yield d, l

    # Convert the data to TensorFlow Datasets
    with tf.device("/CPU:0"):  # else is filled with GPU memory
        dataset = tf.data.Dataset.from_generator(
            generator,
            args=[data_dict["data"], data_dict["label"]],
            output_signature=(
                tf.TensorSpec(shape=(299, 299, 1), dtype=tf.uint8),  # type: ignore
                tf.TensorSpec(shape=(), dtype=tf.uint8), # type: ignore
            ),
        )
        dataset = dataset.shuffle(buffer_size=1024).batch(batch_size)

    return dataset
