# Redidit

## Introduction
  Inspired by Reddit, this is a complete overhaul of a previously completed project: <a href="https://www.github.com/daytonschuh/MockReddit">MockReddit</a>.
  The previous design did not provide ease of use for the end user. Redidit is not built for server deployment, but makes exploration of the APIs prettier and easier to view as an end user. 

## Tech Stack
  - Python
  - Flask
  - Flask_Login
  - Sqlite
  
## Running the Project
  - Clone the repository: ```git clone https://www.github.com/daytonschuh/Redidit```
  - Change to the appropriate directory: ```cd Redidit```
  - To ensure the proper environment, run the series of commands:
  ```
  python3 -m venv auth
  source auth/bin/activate
  pip install flask flask-sqlalchemy flask-login
  export FLASK_APP=redidit
  export FLASK_DEBUG=1
  flask run
  ```
  - Open your browser of choice and go to: ```localhost:5000```<br>
  ***Work In Progress***
