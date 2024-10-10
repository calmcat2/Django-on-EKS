FROM python:3.11

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY ./littlelemon .

# Set the working directory to where manage.py is located
WORKDIR /littlelemon

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "littlelemon","littlelemon.wsgi:application"]