FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ api/

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "-k", "uvicorn.workers.UvicornH11Worker", "api:app", "-b", "0.0.0.0:8000" ]
