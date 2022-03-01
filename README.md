# COMP3106 Project
Full-stack Chess Game with AI integration.

## Team members

- Tom Lam (#)
- Tom Mai (#)
- Minh Thang Cao (101147025)

## Technologies

- **Server**: Flask
- **Client**: React

## Search Algorithms

-
-

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

## Client workflow
_**All must be done in the `/client` directory**_
1. Install `npm` packages: `npm install`
2. Export server's URL: 

    Linux/Mac: `export REACT_APP_SERVER_URL=http://localhost:5000/`

    Windows: `SET REACT_APP_SERVER_URL=http://localhost:5000/`

3. Start the server: `npm start`