# base image
FROM python:3.8-slim

# Execute other installations (from: requirements.txt)
RUN pip install -r requirements.txt

# setting & creating working directory
WORKDIR /app

#copy current directory contents into container(at: /app)
COPY . /app

# command to run the app
CMD ["python3", "clock_app.py"]