FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/enterprise-agent-platform/api:/app/enterprise-agent-platform \
    PORT=8000 \
    APP_TYPE=api

WORKDIR /app/enterprise-agent-platform

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY enterprise-agent-platform/Requirement.txt ./Requirement.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r Requirement.txt

COPY enterprise-agent-platform ./

EXPOSE 8000 8501

COPY start.sh ./
RUN chmod +x ./start.sh
CMD ["./start.sh"]