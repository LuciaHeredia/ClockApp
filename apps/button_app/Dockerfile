# base image
FROM python:3.8

# setting & creating working directory
WORKDIR /app

# copy file (for the RUN command)
# from: the build context(the directory where Dockerfile is located) 
# to:   the current working directory (.) inside the Docker container
COPY requirements.txt .

# Execute other installations (from: requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# copy all files 
# from: the build context(the directory where Dockerfile is located) 
# to:   the current working directory (.) inside the Docker container
COPY . .

# command to run the app
CMD ["python3", "button_app.py"]