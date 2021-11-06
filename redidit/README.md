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
  - Clone the repository ```git clone https://www.github.com/daytonschuh/Redidit```
  - Change to the appropriate directory ```cd Redidit```
  - ```export FLASK_APP=redidit```
  - ```export FLASK_DEBUG=1```
  - Use the command ```flask run```
  - Open your browser of choice and go to ```localhost:5000```<br>
  ***Work In Progress***


## Reset the DataBase
  - In the cloned repository, access python shell ```python3```
  - Import required packages with ```from redidit import db, create_app```
  - Delete the database with ```db.??```
  - Recreate the database with ```db.create_all(app=create_app())```