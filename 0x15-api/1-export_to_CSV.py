#!/usr/bin/python3

"""Using what you did in the task #0, extend your Python script to export data in the CSV format
"""

if __name__ == '__main__':
    import csv
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

    csv_list = [
             [emp_id,
              username,
              emp.get('completed'),
              emp.get('title')] for emp in emp_data]

    with open('{}.csv'.format(emp_id), 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for row in csv_list:
            csv_writer.writerow(row)
