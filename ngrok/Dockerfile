# Gunakan base image Ubuntu 20.04
FROM ubuntu:20.04

RUN echo "Installing OS (apt) dependencies..."
ENV TZ="Asia/Jakarta"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setelah update, instal paket-paket yang diperlukan dalam satu baris perintah
RUN apt-get update && apt-get install -y python3-dev python3-pip

# Instal Flask menggunakan pip3
RUN pip3 install flask

WORKDIR /app

COPY . .
