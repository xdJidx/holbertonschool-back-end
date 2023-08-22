#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests


def all_employed_todo():
    """Displays all tasks for each employed"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users"
    todo_url = f"{base_url}/todos"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_data = {}

    for user in user_data:
        employee_id = user['id']
        employee_username = user['username']

        tasks = [{"username": employee_username,
                  "task": task['title'],
                  "completed": task['completed']}
                 for task in todo_data if task['userId'] == employee_id]
        employee_data[employee_id] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(employee_data, json_file, indent=4)


if __name__ == "__main__":
    all_employed_todo()
