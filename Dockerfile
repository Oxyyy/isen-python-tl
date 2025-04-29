# hadolint global ignore DL3008
FROM debian:12-slim AS build 

# hadolint ignore DL3008
RUN apt-get update && \
    # apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    apt-get install --yes python3-venv=3.10.0-1 gcc=4:10.2.1-1 libpython3-dev=3.10.0-1 && \
    python3 -m venv /venv && \
    # clean apt cache to reduce image size
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

FROM build AS build-venv

COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM gcr.io/distroless/python3-debian12:latest-amd64
COPY --from=build-venv /venv /venv

WORKDIR /app

COPY . .

EXPOSE 8080

ENTRYPOINT ["/venv/bin/python"]
CMD ["manage.py", "runserver", "0.0.0.0:8080"]