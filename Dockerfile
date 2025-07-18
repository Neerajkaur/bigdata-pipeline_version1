FROM python:3.10

WORKDIR /app
COPY app.py .
COPY data.csv .

RUN pip install pandas

CMD ["python", "app.py"]