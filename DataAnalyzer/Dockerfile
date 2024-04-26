# Use an appropriate base image
FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app


# Copy the data updater code into the container
COPY requiernemts.txt /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requiernemts.txt

COPY /app /app

# Expose any necessary ports
# EXPOSE 5000

# Specify the command to run the data updater service
CMD ["python", "/app/DataAnalyzer.py"]
