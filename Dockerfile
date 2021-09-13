FROM python:3.9.6

ARG target="."

ENV PYTHONPATH=/usr/src/app/

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY setup.py /usr/src/app/
COPY README.md /usr/src/app/
COPY CHANGES.md /usr/src/app/
COPY pairing/__init__.py /usr/src/app/pairing/

RUN pip install --no-cache-dir -e "${target}"

COPY . /usr/src/app
