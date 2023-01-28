FROM python:3.11-slim

WORKDIR /skywars
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD flask run -h 0.0.0.0 -p 80