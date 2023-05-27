#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress.
"""
import requests
import sys
import json


if __name__ == "__main__":
    restapi = "https://jsonplaceholder.typicode.com/"
    user = requests.get(restapi + "users/{}".format(sys.argv[1])).json()
    todores = requests.get(restapi + "todos", params={"userId": sys.argv[1]})
    todo = todores.json()
    username = user.get("username")
    user_id = sys.argv[1]

    with open('{}.json'.format(user_id), 'w') as filename:
        json.dump({user_id: [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": username}
                             for task in todo]}, filename)
