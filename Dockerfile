FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean;

# Optionally create symbolic links to python and pip
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install PPA
RUN apt-get update && \
    apt-get install software-properties-common -y && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update;

# Install Java 8
RUN apt-get install -y openjdk-8-jdk && \
    apt-get clean;

# Python and Poetry setup
ENV \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.2

RUN pip3 install poetry==${POETRY_VERSION}

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry install  --no-interaction --no-ansi

COPY . .