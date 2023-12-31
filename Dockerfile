# Set base image (host OS)
FROM python:3.11-alpine

# Add variables
ENV FLASK_APP=api/app.py

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY api/. /app/api/.

# For docs
COPY docs/ /app/docs/.

# Specify the command to run on container start
CMD [ "flask", "run", "--host", "0.0.0.0" ]
