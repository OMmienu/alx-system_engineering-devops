#!/usr/bin/python3

"""Using what you did in the task #0, 
extend your Python script to export data in the JSON format
"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

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
    username = user_data.get('username')

    data = [
             {"task": todo.get('title'),
              "completed": todo.get('completed'),
              "username": username} for todo in emp_data]
    new_data = {emp_id: data}

    with open('{}.json'.format(emp_id), 'w') as f:
        json.dump(new_data, f)
