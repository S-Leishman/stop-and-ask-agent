FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOST=0.0.0.0 \
    PORT=8080 \
    AEVION_STATE_DIR=/tmp/vetproof

WORKDIR /app
COPY requirements.lock requirements.txt ./
RUN pip install --no-cache-dir -r requirements.lock
COPY app ./app
COPY ui ./ui
COPY data/task_brief.txt ./data/task_brief.txt
COPY server.py demo.py ./

EXPOSE 8080
CMD ["python", "server.py"]
