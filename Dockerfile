
FROM python:3.9-slim

WORKDIR /app

RUN pip install Flask==1.1.4 MarkupSafe==2.0.1

COPY . .

EXPOSE 5003

CMD ["python3", "app.py"]
