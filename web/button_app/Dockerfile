# base image
FROM python:3.8-slim

# setting & creating working directory
WORKDIR /app

#copy current directory contents into container(at: /app)
COPY . /app

# Execute other installations (from: requirements.txt)
RUN pip install -r requirements.txt

# command to run the app
CMD ["python3", "button_app.py"]