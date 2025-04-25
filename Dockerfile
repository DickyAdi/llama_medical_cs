FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY medical_cs /app/medical_cs

EXPOSE 8000

CMD ["uvicorn", "medical_cs.main:app", "--host", "0.0.0.0", "--port", "8000"]