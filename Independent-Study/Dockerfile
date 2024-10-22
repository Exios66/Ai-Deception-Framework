# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from the host to the container
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt
# The --no-cache-dir flag reduces the image size by not caching the downloaded packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code from the host to the container
COPY . .

# Specify the command to run when the container starts
# This runs the uvicorn server, which serves the FastAPI application
# The main:app refers to the app object in main.py
# --host 0.0.0.0 allows the server to accept connections from any IP
# --port 8000 specifies the port on which the server will listen
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
