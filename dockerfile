FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        netbase \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 80

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=80", "--server.address=0.0.0.0"]