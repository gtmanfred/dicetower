FROM debian:sid-slim
WORKDIR /app
CMD /usr/bin/python3 -m poetry run python -m wsgi
EXPOSE 8000

RUN apt update && \
    apt install -y \
        python3 \
        python3-pip \
        python3-venv \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*

ADD pyproject.toml .
ADD package.json .

RUN npm install && \
    python3 -m pip install poetry && \
    python3 -m poetry config virtualenvs.path /app/.cache/pypoetry/virtualenvs/ && \
    python3 -m poetry install --no-dev --no-root && \
    rm -rf /app/.cache/pypoetry/cache /root/.cache/pip

COPY ./ .

RUN npm run build
