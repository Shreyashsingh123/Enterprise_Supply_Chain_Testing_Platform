#!/bin/sh

APP_TYPE=${APP_TYPE:-streamlit}
PORT=${PORT:-8501}

if [ "$APP_TYPE" = "streamlit" ]; then
  echo "Starting Streamlit on port $PORT"
  streamlit run froontent.py --server.address 0.0.0.0 --server.port "$PORT"
else
  echo "Starting Uvicorn API on port $PORT"
  uvicorn api.main:app --host 0.0.0.0 --port "$PORT"
fi
