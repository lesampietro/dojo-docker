FROM ubuntu:22.04

RUN apt update && apt install -y \
    curl \
    vim \
    git \
    python3 \
    python3-pip

RUN pip3 install flask

RUN echo "olha eu aqui tbm"

CMD ["tail", "-f", "/dev/null"]
