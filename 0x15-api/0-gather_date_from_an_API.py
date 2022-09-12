#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv

if _name_ == '_main_'
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}."
                        format(userId), verify=False).json()
    todo = request.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json)
    complete_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with task({}/{}):".
            format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
