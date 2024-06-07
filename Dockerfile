FROM python:3.9

WORKDIR /code_gsg

COPY . /code_gsg

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    libv4l-dev

RUN pip install --no-cache-dir opencv-python

CMD ["python3", "code_gsg.py"] 