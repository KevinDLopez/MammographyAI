# docker run -it --rm --gpus all -p 8888:8888 -v C:/Repositories/School/Semester3/CECS_550/FinalProject:/tf tensorflow/tensorflow:latest-gpu-jupyter


# Use the tensorflow/tensorflow:latest-gpu-jupyter image as the base
FROM tensorflow/tensorflow:latest-gpu-jupyter

# Set the working directory in the container
WORKDIR /tf

# Copy the current directory contents into the container at /tf
# COPY . /tf

# Install the required python packages
RUN pip install scikit-learn seaborn pandas opencv-python scikit-image preprocessing tqdm imageio

RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN echo "Done installing packages"
# Make port 8888 available to the world outside this container
EXPOSE 8888

# Run jupyter notebook when the container launches
# CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]