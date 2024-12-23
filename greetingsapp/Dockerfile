
FROM ubuntu:latest

# Set the working directory for subsequent commands
WORKDIR /app



# Copy the requirements.txt file before creating the virtual environment
COPY . /app

# Install dependencies for Python, pip, and virtual environment
RUN apt update && \
    apt install -y python3 python3-pip python3-venv

# Create a virtual environment in the container
RUN python3 -m venv /venv

# Install the dependencies using pip inside the virtual environment
RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /app/requirements.txt
   
# Expose port 8000 for Django
EXPOSE 8000

# Set the entrypoint to use the virtual environment for running Django
ENTRYPOINT ["/venv/bin/python3"]

# Run the Django development server
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
