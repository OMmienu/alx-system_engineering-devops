#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

if__name__== '__main__':
    import requests
    import sys import argv

    emp_id = int(argv[1])
    todos = requests.get(
          'https://jsonplaceholder.typicode.com/todos/')
    users = requests.get(
          'https://jsonplaceholder.typicode.com/users/{}'.
          format(emp_id))

    todos_data = todos.json()
    user_data = users.json()

    emp_data = list(filter(
            lambda emp: emp_id == emp.get('userId'), todos_data))
    num_tasks = len(emp_data)
    done_tasks = len(list(filter(
               lambda done: done.get('completed'), emp_data)))
    emp_name = user_data.get('name')

    print("Employee {} is done with tsks ({}/{}):".format
            emp_name, done_tasks, num_tasks))

    for task in emp_data:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
