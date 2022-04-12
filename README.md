# COMP3106 Project
Full-stack Chess Game with AI integration.

## Team members

- Tom Lam (101114541)
- Tom Mai (101128263)
- Minh Thang Cao (101147025)

## Technologies

- **Server**: Flask
- **Client**: React

## New workflow
_**All must be done in the main (`/`) cloned directory**_
1. Setup server (need to be done only one for new cloned repo):
```bash
./run.sh -f
```
2. Start server:
```bash
./run.sh -s
```
3. Start client (in a separate terminal instance):
```bash
./run.sh -c
```

## Legacy workflow
### Server workflow
_**All must be done in the `/server` directory**_

1. Create env:
```bash
python3 -m venv venv
```
2. Activate env: 

- Linux/Mac:
```
source ./venv/bin/activate
```

- Different platform: [see docs](https://flask-socketio.readthedocs.io/en/latest/)

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Export flask app env variable:

- Linux/Mac:
```
export FLASK_APP=server FLASK_ENV=development
```

- Windows:
```
SET FLASK_APP=server | FLASK_ENV=development
```

5. Run server:
```
flask run
```

### Client workflow
_**All must be done in the `/client` directory**_
1. Install `npm` packages:
```bash
npm install
```
2. Export server's URL: 
- Linux/Mac:
```
export REACT_APP_SERVER_URL=http://127.0.0.1:5000/api
```

- Windows:
```
SET REACT_APP_SERVER_URL=http://127.0.0.1:5000/api
```

3. Start the server:
```
npm start
```
