#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    restapi = "https://jsonplaceholder.typicode.com/"
    user = requests.get(restapi + "users/{}".format(sys.argv[1])).json()
    todores = requests.get(restapi + "todos", params={"userId": sys.argv[1]})
    todo = todores.json()
    name = user.get("username")

    with open('{}.csv'.format(user_id), 'w') as file:
        for task in todo:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, name, task.get('completed'),
                               task.get('title')))
