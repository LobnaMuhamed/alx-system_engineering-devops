#!/usr/bin/python3
"""
Write a Python script that,
using this REST API, for a given employee ID,
returns information about
his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    if (len(argv) == 2):
        id = int(argv[1])
        url_user = f"https://jsonplaceholder.typicode.com/users/{id}"
        user = requests.get(url_user).json()
        url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
        todo = requests.get(url_todo).json()
        total_tasks = len(todo)
        done_filter = list(filter(lambda obj: obj['completed'], todo))
        len_done_filter = len(done_filter)
        print(f"Employee {user['name']} is done with \
tasks({len_done_filter}/{total_tasks}):")
        for task in done_filter:
            print("\t ", end='')
            print(task['title'])
