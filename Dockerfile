# Dockerfile
# Uses multi-stage builds requiring Docker 17.05 or higher
# See https://docs.docker.com/develop/develop-images/multistage-build/
# Inspiration: https://github.com/svx/poetry-fastapi-docker

# ===================================================
# contains shared environment variables
# ===================================================

FROM python:3.10-slim-bullseye

ARG PYPI_USER
ARG PYPI_PASSWORD
ARG ENVIRONMENT

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1 \
    LANG=pt_BR.UTF-8 \
    LANGUAGE=pt_BR:pt_br \
    LC_ALL=pt_BR.UTF-8 \
    NEW_RELIC_CONFIG_FILE=/code/newrelic.ini \
    DJANGO_SETTINGS_MODULE=enpyre_play.settings

ENV PATH="$POETRY_HOME/bin:$PATH"

# ====================================================================
# build dependencies
# ====================================================================

RUN apt-get update \
    && apt-get install -y \
      curl \
      libpq-dev \
      gnupg2 \
      gcc \
      netcat \
      net-tools \
      vim \
      nano \
      git \
      make \
      ca-certificates \
      locales \
      locales-all \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates \
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo 'America/Sao_Paulo' > /etc/timezone \
    && rm -rf /var/lib/apt/lists/*

# Install doppler
RUN curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | apt-key add - \
    && echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list
RUN apt update -y && apt install -y doppler

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
ENV POETRY_VERSION=1.3.2
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} \
    && chmod a+x /opt/poetry/bin/poetry

# Create workdir
RUN mkdir /code
WORKDIR /code

# Install newrelic
RUN pip install --upgrade pip && pip install --no-cache-dir newrelic
ENV PATH="${PATH}:/code/.local/bin"

# Install dependencies
COPY ./poetry.lock ./pyproject.toml ./install.sh ./
RUN ./install.sh

# # ADD APP
COPY . .

ENTRYPOINT ["doppler", "run", "--"]
CMD ["./start.sh"]
