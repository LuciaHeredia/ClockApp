## Clock App Missions: 
### Clock App (clock_app): 
-	It displays the current time. 
-	Exposes an **API endpoint** to decrement the time.
<img src = "screenshots/LUCIA HEREDIA.png">

### Button App (button_app):
-	Contains a button to decrement the time. 
-	Communicates with the **clock_app** by making a POST request to the **API endpoint**.
<img src = "screenshots/LUCIA HEREDIA.png">

## Structure:
```
project_folder/
├── apps/
│   ├── clock_app/
│   │   ├── clock_app.py
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── templates/
│   │       └── ...
│   └── button_app/ 
│       ├── button_app.py
│       ├── Dockerfile
│       ├── requirements.txt
│       ├── templates/
│           └── ...
└── docker-compose.yml 
```

## Steps:
### Create Flask Apps:
-	Create two directories: **clock_app** and **button_app**. 
-	In each directory: create Python files (**app.py**) and templates(**index.html**). 
-   In the Python files: **button_app** communicates with **clock_app** using the *requests* library. 
-	**clock_app**: Displays the current time and updates it upon **API endpoint** request (/update_time) . 
-	**button_app**: Contains a button to decrement the time and communicates with **clock_app** via **API endpoint**. 
-	Set up **requirements.txt** file in each directory: *Flask*, *requests*.
### Create Dockerfiles:
-	In each directory, create a **Dockerfile** specifying the Docker image configuration. 
### Create Docker Compose File:
-	Create a **docker-compose.yml** file in the project root. 
-	Define services for both **clock_app** and **button_app**, specifying: *build contexts*, *ports* and *environment*(in **button_app**). 
-	Configure a default *network* for communication between the two containers. 
-	Build and Run the Containers:
    ```
    docker-compose up --build
    ```
### Access the Apps:
-	The **clock_app** is available at http://localhost:5001. 
-	The **button_app** is available at http://localhost:5002. 
