# Use an official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Django port
EXPOSE 8000

# Run the application using Gunicorn
CMD ["gunicorn", "automated.wsgi:application", "--bind", "0.0.0.0:8000"]
