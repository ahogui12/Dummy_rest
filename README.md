# Dummy_rest

## Presentation
Little project to ramp up on REST APIs with Docker
This is a dummy application, Errors are not handled at all

## Usage
This "project" has two parts, a python REST server to handle POST and GET on entire files, and its container to deploy it easily
You can run the server only with python and try the commands.

## Standalone
Assuming that you have pip installed

   pip install Flask

   python api.py

The application is designed to send the files to /tmp, if you want to change the location please update the file `api.py`

   ...
   UPLOAD_FOLDER = '/tmp'
   ...

## Docker install

   docker build -t dummy_rest:latest .

   docker run -d -p 5000:5000 dummy_rest

### POST
Idea here is to POST entire files

    curl -X POST -F "file=@path_to_my_file" http://localhost:5000

You should have a 302 message as a return saying that your file was redirected, but no issue here (behavior to be modified of course)

### GET
    curl -X GET http://localhost:5000
    [
      "my_file"
    ]
