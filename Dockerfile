# Use an official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python requirements file into the container
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code into the container
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port 5000 for Flask
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
