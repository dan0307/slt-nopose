# Use an official Python runtime as the base image
FROM python:3-alpine3.11

# Install git and other necessary build dependencies
RUN apk update && apk add --no-cache git build-base cmake linux-headers

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

ENV PIP_DEFAULT_TIMEOUT=500

# Run app.py when the container launches
CMD python ./main.py

