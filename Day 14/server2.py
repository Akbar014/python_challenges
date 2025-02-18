
import os 
import datetime
from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save

app = FastAPI()


@app.get("/")
def hello_world():
    return {'data': 'world'}

@app.get("/abc")
def abc():
    return {'data': [1,2,3]}


@app.post("/box-office-mojo-scrapper")
def box_office_scrapper():
    scrape_runner()
    trigger_log_save()
    return {"data": [1,2,3]}

