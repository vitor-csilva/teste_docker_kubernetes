FROM python:3.8.13-alpine3.16

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV TWORPTEST "true100%"

RUN export TWORPTEST >> .bashrc

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]