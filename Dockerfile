FROM debian:sid-slim
WORKDIR /app
CMD python3 -m poetry run uvicorn --host 0.0.0.0 wsgi:app
EXPOSE 8000

RUN apt update && \
    apt install -y \
        python3 \
        python3-pip \
        python3-venv \
        nodejs \
        npm

ADD pyproject.toml .
ADD package.json .

RUN npm install && \
    python3 -m pip install poetry && \
    python3 -m poetry install

COPY ./ .

RUN npm run build
