#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    restapi = "https://jsonplaceholder.typicode.com/"
    user = requests.get(restapi + "users/{}".format(sys.argv[1])).json()
    todores = requests.get(restapi + "todos", params={"userId": sys.argv[1]})
    todo = todores.json()
    name = user.get("username")

    cdone = 0
    done = []

    for task in todo:
        if task.get('completed'):
            done.append(task)
            cdone += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, cdone, len(todo)))

    for task in done:
        print("\t {}".format(task.get('title')))
