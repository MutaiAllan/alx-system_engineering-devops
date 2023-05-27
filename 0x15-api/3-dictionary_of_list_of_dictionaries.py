#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    restapi = "https://jsonplaceholder.typicode.com/"
    users = requests.get(restapi + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(restapi + "todos",
                                       params={"userId": user.get("id")})
                                       .json()]
            for user in users}, jsonfile)
