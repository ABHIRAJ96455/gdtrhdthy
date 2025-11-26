FROM python:3.9-slim-buster

# Install system dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt /tmp/requirements.txt

# Install python dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt

# Set working directory
WORKDIR /MusicPlayer

# Copy all bot files into container
COPY . /MusicPlayer

# Copy startup script
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

# Run bot
CMD ["/bin/bash", "/startup.sh"]
