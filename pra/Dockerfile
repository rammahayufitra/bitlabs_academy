# Gunakan base image Ubuntu 20.04
FROM ubuntu:20.04

RUN echo "Installing OS (apt) dependencies..."
ENV TZ="Asia/Jakarta"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setelah update, instal paket-paket yang diperlukan
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    pkg-config \
    libgtk2.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libatlas-base-dev \
    gfortran \
    python3-dev \
    python3-pip \
    libgl1-mesa-glx

RUN pip3 install opencv-python

WORKDIR  app

COPY . . 



