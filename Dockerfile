## To swap between pypy and CPython (vanilla python)
## change the FROM line below and rebuild the container image.
## Alternatively you can also build two images like so:
## docker build -t pypy-benchmarking:0.1 .
## change the FROM line to python:3.11.7
## docker build -t python-benchmarking:0.1 .
## run your two different containers (pypy-benchmarking:0.1 and python-benchmarking:0.1)

FROM pypy:3.10

# FROM python:3.11.7
# FROM python:3.12.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install python dependencies
RUN pip install -r requirements.txt

# Configure ports
EXPOSE 4000

# Run the chmod command to change permissions on application startup script
RUN chmod 755 /app/run_app.sh

# Default environmental variables
ENV HTTPPORT 4000
ENV KEEP_ALIVE 65
ENV GRACEFUL_TIMEOUT 60
ENV CONCURRENT_CONNECTIONS 800
ENV LISTEN_SLOTS 3584
ENV AWS_REGION US-WEST-2

ENTRYPOINT ["/app/run_app.sh"]