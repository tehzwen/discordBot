FROM python:3.10

RUN mkdir -p /app
RUN apt update && apt upgrade -y
RUN apt install -y gcc iputils-ping wakeonlan
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
