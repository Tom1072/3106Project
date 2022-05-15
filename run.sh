#! /bin/bash

first_time_setup=""
prepare_production=""
test_run_production=""
run_dev_client=""
run_dev_server=""

while getopts "fptcs" flag; do
    case "${flag}" in
        f) first_time_setup="true" ;;    # First time setup
        c) run_dev_client="true" ;;      # Run dev client
        s) run_dev_server="true" ;;      # Run dev server
        t) test_run_production="true" ;; # Rebuild and test run production app
        p) prepare_production="true" ;;  # Prepare production envirnonment (used only by Procfile)
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

if [[ ${test_run_production} == "true" ]]; then
    # Prereqs: run.sh -f
    echo "Setting up production environment..."

    export REACT_APP_SERVER_URL=/api
    export FLASK_APP=./server/server:app FLASK_ENV=deployment
    cd ./client
    npm run build
    cd ..

    echo "Test running production..."
    source ./venv/bin/activate
    flask run
fi


if [[ ${prepare_production} == "true" ]]; then
    # Only used by Procfile
    export REACT_APP_SERVER_URL=/api
fi
