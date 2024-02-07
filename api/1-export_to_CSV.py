#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import requests
from sys import argv


if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    users_url = main_url + "/users"
    todos_url = main_url + "/todos"

    users_result = requests.get(users_url).json()
    todos_result = requests.get(todos_url).json()

    for user in users_result:
        if user['id'] == int(argv[1]):
            user_name = user['username']
    with open('{}.csv'.format(argv[1]), 'w') as f:
        for todo in todos_result:
            if todo['userId'] == int(argv[1]):
                task = todo['completed']
                title = todo['title']
                f.write(
                    f"\"{argv[1]}\",\"{user_name}\",\"{task}\",\"{title}\"\n")
