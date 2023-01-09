# movie-api
An API that does CRUD operation on a film database

## About the Project 

During my first year at [ITS ICT Piemonte](https://www.its-ictpiemonte.it) I attended a RESTful API course to get an introduction about this tecnology and how to use it. The main example was a movie API developed by my teacher used to test various type of endpoint using [Insomia](https://insomnia.rest). In this repo I redevelop the movie api using the [documentation](./docs.yaml) about its use left by my teacher. The project will be also deployd [on railway.app](https://railway.app)

## Requirements

To run the project on localhost you need a version of python at least 3.10.* and the libraries in [requirements](./requirements.txt)

To install the you can run the following command in your terminal:

```python
pip install fastapi
pip install uvicorn
pip install pandas
```

## Run the project 

After your system satisfy the requirements use your terminal to navigate to the folder that contain the project and run 

```python
uvicorn main:app
```

Then paste in your browser the following URL 
```
http://127.0.0.1:8000/docs
```
To see the documentation generated with FastAPI