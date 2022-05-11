#! /bin/bash

prepare_development=""
prepare_production=""
run_production=""
run_dev_client=""
run_dev_server=""

while getopts "dptcs" flag; do
    case "${flag}" in
        d) prepare_development="true" ;;
        p) prepare_production="true" ;;
        t) run_production="true" ;;
        c) run_dev_client="true" ;;
        s) run_dev_server="true" ;;
    esac
done

if [[ ${prepare_development} == "true" ]]; then
    echo "Setting up client and server for development..."
    rm -rf venv
    python3 -m venv venv
    source ./venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

    cd ./client
    rm -rf ./node_modules
    npm i
    
    cd ..
elif [[ ${prepare_production} == "true" ]]; then
    echo "Setting up client and server for production..."
    rm -rf venv
    python3 -m venv venv
    source ./venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

    cd ./client
    rm -rf ./node_modules
    npm i

    export REACT_APP_SERVER_URL=/api
    npm run build
    cd ..
fi

if [[ ${run_production} == "true" ]]; then
    export REACT_APP_SERVER_URL=/api
    export FLASK_APP=./server/server:app FLASK_ENV=deployment
    source ./venv/bin/activate
    flask run
elif [[ ${run_dev_client} == "true" ]]; then
    cd ./client
    export REACT_APP_SERVER_URL=http://127.0.0.1:5000/api
    npm start
    cd ..
elif [[ ${run_dev_server} == "true" ]]; then
    source ./venv/bin/activate
    export FLASK_APP=./server/server:app FLASK_ENV=development
    flask run
fi
