from flask import request

from server import app
from server.service import laptop_service


@app.post("/laptop")
def create_laptop():
    laptop = request.get_json()
    error = laptop_service.create_laptop(laptop)
    if error is not None:
        return error, 400
    return laptop, 201


@app.get("/laptop")
def get_all_laptops():
    laptop = laptop_service.show_laptop()
    return laptop


@app.delete("/laptops")
def delete_laptops():
    laptop_service.delete_all_laptops()
    return {"status": "The table is empty"}


@app.delete("/laptop/<int:id>")
def delete_lap_id(id):
    print("delete laptop by id", id)
    laptop_service.delete_lap(id)
    return {}


@app.put("/laptop/<int:id>")
def update_laptop(id):
    laptop = request.get_json()
    laptop_service.put_lap(id, laptop)
    return laptop
