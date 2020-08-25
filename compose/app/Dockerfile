FROM python:3.8-alpine3.11

ENV PROJECT_ROOT_DIR /application
ENV SOURCE_DIR $PROJECT_ROOT_DIR/server
ENV STATIC_FILES_DIR $PROJECT_ROOT_DIR/static
ENV TEMPLATE_DIR $PROJECT_ROOT_DIR/templates
ENV PATH=$PATH:$PROJECT_ROOT_DIR/scripts/

ENV RUNTIME_PACKAGES \
    libev \
    pcre \
    docker \
    jpeg-dev \
    zlib-dev \
    libressl-dev \
    libffi-dev \
    openssh \
    python-dev

ENV BUILD_PACKAGES \
    libev-dev \
    git \
    build-base \
    pcre-dev \
    gcc \
    linux-headers \
    make

RUN apk update && \
    apk upgrade && \
    pip install --upgrade pip && \
    pip install wheel pipenv

RUN apk --no-cache add --virtual build-deps $BUILD_PACKAGES && \
    apk --no-cache add $RUNTIME_PACKAGES

RUN mkdir $PROJECT_ROOT_DIR

COPY Pipfile $PROJECT_ROOT_DIR
COPY Pipfile.lock $PROJECT_ROOT_DIR

WORKDIR $PROJECT_ROOT_DIR

RUN pipenv install --deploy --system --dev

COPY server $SOURCE_DIR
COPY templates $TEMPLATE_DIR
COPY scripts $PROJECT_ROOT_DIR/scripts
COPY static $STATIC_FILES_DIR

RUN ls $PROJECT_ROOT_DIR
RUN ls $PROJECT_ROOT_DIR/scripts

RUN chmod +x $PROJECT_ROOT_DIR/scripts/runserver

CMD runserver