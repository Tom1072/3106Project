#! /bin/bash

echo "Setting up client and server..."
cd ./client
rm -rf ./node_modules
npm i

cd ../server
rm -rf venv
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

cd ../client
export REACT_APP_SERVER_URL=/api
npm run build
cd ../server
source ./venv/bin/activate
export FLASK_APP=server:app FLASK_ENV=deployment
