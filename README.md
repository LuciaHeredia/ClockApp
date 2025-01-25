# Clock App
## Structure:
```
project_folder/
├── web/
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

## App Missions: 
### Clock App (clock_app): 
-	It displays the current time. 
-	Exposes an API endpoint (/update_time) to decrement the time. 
### Button App (button_app):
-	Contains a button to decrement the time. 
-	Communicates with the clock_app by making a POST request to the /update_time API endpoint.

