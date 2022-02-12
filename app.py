from flask import Flask
# For the above line to run correctly, had to press command+shift+P and then type Python: Select Interpreter and select PythonData or python3 (whichever is desired)
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
# in command line we create the environment for flask running the line export FLASK_APP=app.py
# then in the correct folder/directory (surfs-up) run the line flask run and you will see running on with a local host
# when the local host is copied and pasted into a web browser, then the output is Hello world
