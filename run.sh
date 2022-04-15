#! /bin/bash

first_flag=""
client_flag=""
server_flag=""

while getopts "fcs" flag; do
    case "${flag}" in
        f) first_flag="true" ;;
        c) client_flag="true" ;;
        s) server_flag="true" ;;
    esac
done

if [[ ${first_flag} == "true" ]]; then
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
    
    cd ..
fi

if [[ ${client_flag} == "true" ]]; then
    cd ./client
    export REACT_APP_SERVER_URL=http://localhost:5000/api
    npm start
    cd ..
elif [[ ${server_flag} == "true" ]]; then
    cd ./server
    source ./venv/bin/activate
    export FLASK_APP=server FLASK_ENV=development
    flask run
    cd ..
fi