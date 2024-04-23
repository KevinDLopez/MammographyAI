import tensorflow as tf
from typing import List, Tuple, TypedDict

data_type = TypedDict("data_type", {"label": tf.Tensor, "image": tf.Tensor})


def read_data(filename):
    features = {
        "label": tf.io.FixedLenFeature([], tf.string),
        "image": tf.io.FixedLenFeature([], tf.string),
    }

    raw_data = tf.data.TFRecordDataset([filename])

    # Define a function to parse the tfrecord files
    def parse_function(example_proto):
        return tf.io.parse_single_example(example_proto, features)

    parsed_dataset = raw_data.map(parse_function)

    data: List[data_type] = []

    # data preprocessing - convert the image and label to the correct shape
    for element in parsed_dataset:
        image = tf.reshape(tf.io.decode_raw(element["image"], tf.uint8), [640, 640])
        label = tf.reshape(tf.io.decode_raw(element["label"], tf.uint8), [640, 640])
        data.append({"label": label, "image": image})
    return data
