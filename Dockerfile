FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get clean all

RUN pip3 install flask

COPY state /app
WORKDIR /app

CMD ["python3", "stateless.py"]

