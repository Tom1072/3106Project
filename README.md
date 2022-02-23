# 3106Project
AI Chessgame

## Server workflow
_**All must be done in the `/server` directory**_

1. Create env: `python3 -m venv venv`
2. Activate env: 

    Linux/Mac: `source ./venv/bin/activate`
    Different platform: [see docs](https://flask-socketio.readthedocs.io/en/latest/)

3. Install dependencies: `pip install -r requirements.txt`
4. Export flask app env variable: 

    Linux/Mac: `export FLASK_APP=server FLASK_ENV=development`
    Windows: `SET FLASK_APP=server | FLASK_ENV=development`

5. Run server: `flask run`