from flask import request

from server import mysql
from server.db import laptop_repository

def create_laptop(laptop):
    print(f"create a laptop:", laptop)
    all_laptops = laptop_repository.get_laptop(mysql)
    name = laptop['name']
    year = laptop['year']

    for ex_laptop in all_laptops:
        if ex_laptop['name'] == name:
            return{"error": "laptop with this name already exists"}
        if ex_laptop['year'] == year:
            return{"error": "laptop with this year already exists"}

    laptop_repository.post_laptop(mysql, laptop)
    return None

def show_laptop():
    laptop = laptop_repository.get_laptop(mysql)
    print("all laptops:", laptop)
    return laptop

def delete_all_laptops():
    laptop_repository.delete_all_laptops(mysql)

def delete_lap(id):
    laptop_repository.delete_id_lap(mysql,id)


def put_lap(id, laptop):
    laptop_repository.update_lap(mysql, id, laptop)
    print("update laptop", id)