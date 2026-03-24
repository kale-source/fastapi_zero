from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from async_project.schemas import Message

app = FastAPI(title='Async Project API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def first_route():
    return {'message': 'Hello World'}


@app.get('/html_response', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def second_route():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Route Response - fastAPI</title>
</head>
<body>
    <p>Hello World!</p>
</body>
</html>"""
