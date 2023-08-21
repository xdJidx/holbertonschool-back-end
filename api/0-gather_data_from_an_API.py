#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def Employed_todo(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data['name']
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])
    completed_tasks_titles = [task['title']
                              for task in todo_data if task['completed']]

    print(f"Employee {employee_name} "
          "is done with tasks({done_tasks}/{total_tasks}):")
    for title in completed_tasks_titles:
        print(f"\t{title}")


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    Employed_todo(employee_id)
