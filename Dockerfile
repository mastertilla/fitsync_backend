FROM python:3.12.1 AS builder

ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3
ENV PATH="/root/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -

# Install dependencies in an intermidate container
WORKDIR /app
COPY poetry.toml poetry.lock pyproject.toml /app/

RUN poetry config installer.max-workers 10

# Remove unnecessary files
RUN poetry install --without dev

FROM python:3.12.1-slim

ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin/:${PATH}"
ENV PYTHONPATH="/app/.venv/lib/python3.11/site-packages:${PYTHONPATH}"
ENV VIRTUAL_ENV="/app/.venv"

RUN  apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
  unzip curl \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=builder /app/.venv/ /app/.venv
COPY . /app

EXPOSE 8000

ENTRYPOINT ["python", "-m", "main"]
