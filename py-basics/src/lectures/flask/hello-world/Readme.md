# Flask Demo

## How to exetute...

In order to run this demo...

1. ...open a Powershell terminal and execute these commands

    ```powershell
    # actives the virtual environment and passes the app's name to the variable FLASK_APP
    venv\Scripts\activate
    $env:FLASK_APP = "hello"
    $env:FLASK_ENV = "debugging"
    
    #starts the application
    flask run
    ```
