FROM python:3.10-slim as build
# Install dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential gcc

# Create virtual environment
WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# From this new container...
FROM python:3.10-slim@sha256:54956d6c929405ff651516d5ebbc204203a6415c9d2757aaddcde35be680431e
# Run the container with the least possible privileges
RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

RUN mkdir /usr/app && chown python:python /usr/app
WORKDIR /usr/app

# Copy required files from the build container
COPY --chown=python:python --from=build /usr/app/venv ./venv
COPY --chown=python:python . .

USER 999

# Run the server
ENV PATH="/usr/app/venv/bin:$PATH"
CMD ["python", "main.py"]
