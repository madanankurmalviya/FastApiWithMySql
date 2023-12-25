from typing import Union

from fastapi import FastAPI

from db_helper import get_customer_status, get_employees_status

app = FastAPI()


@app.get("/")
def read_root():
    return {get_employees_status(1002)}
    return {get_customer_status('Atelier graphique')}
