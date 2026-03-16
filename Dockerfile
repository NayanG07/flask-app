FROM python:3.13-slim

WORKDIR /apps

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]