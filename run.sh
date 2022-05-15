#! /bin/bash

first_time_setup=""
prepare_production=""
test_run_production=""
run_dev_client=""
run_dev_server=""

while getopts "fptcs" flag; do
    case "${flag}" in
        f) first_time_setup="true" ;;
        p) prepare_production="true" ;;
        t) test_run_production="true" ;;
        c) run_dev_client="true" ;;
        s) run_dev_server="true" ;;
    esac
done

if [[ ${first_time_setup} == "true" ]]; then
    # Run this script to setup a fresh environemnt (for both dev and prod environments)
    echo "Installing dependencies..."
    rm -rf venv
    python3 -m venv venv
    source ./venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

    cd ./client
    rm -rf ./node_modules
    npm i
    
    cd ..
fi

if [[ ${prepare_production} == "true" ]]; then
    # Prereqs: run.sh -f
    echo "Setting up production environment..."

    export REACT_APP_SERVER_URL=/api
    cd ./client
    npm run build
    cd ..
fi

if [[ ${test_run_production} == "true" ]]; then
    # Prereqs: run.sh -f && run.sh -p
    echo "Test running production..."
    export FLASK_APP=./server/server:app FLASK_ENV=deployment
    source ./venv/bin/activate
    flask run
fi

if [[ ${run_dev_client} == "true" ]]; then
    # Prereqs: run.sh -f
    echo "Running development client..."
    cd ./client
    export REACT_APP_SERVER_URL=http://127.0.0.1:5000/api
    npm start
    cd ..
elif [[ ${run_dev_server} == "true" ]]; then
    # Prereqs: run.sh -f
    echo "Running development server..."
    source ./venv/bin/activate
    export FLASK_APP=./server/server:app FLASK_ENV=development
    flask run
fi
