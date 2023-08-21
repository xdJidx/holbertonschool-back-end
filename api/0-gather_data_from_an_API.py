#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID.
"""


import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = f"{base_url}/users/{employee_id}"
    todo = f"{base_url}/todos?userId={employee_id}"

    response_user = requests.get(user_id)
    response_todo = requests.get(todo)

    user_data = response_user.json()
    todo_data = response_todo.json()

    name = user_data['name']

    todo_done = sum(1 for task in todo_data if task['completed'])
    todo_count = len(todo_data)

    list_task_complete = [task['title']
                          for task in todo_data if task['completed']]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_done, todo_count))

    for title in list_task_complete:
        print("\t {}".format(title))