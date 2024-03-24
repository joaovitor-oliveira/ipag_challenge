FROM python:3.9-slim

WORKDIR /home/python/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["tail", "-f", "/dev/null"]