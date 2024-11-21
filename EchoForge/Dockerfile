# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements.txt into the container
COPY ./requirements.txt /code/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY ./ /code/

# Set environment variable to ensure Python output is not buffered
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for Django
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
