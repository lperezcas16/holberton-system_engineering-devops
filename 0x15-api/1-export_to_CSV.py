#!/usr/bin/python3
"""
export data in the CSV format.
"""
import requests
import sys


if __name__ == "__main__":
    user_id = ""
    try:
        user_id = sys.argv[1]
    except:
        pass

    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    rq_user = requests.get(url=url)
    url += "/todos"
    rq_todos = requests.get(url=url)

    if rq_todos.status_code >= 300:
        print(rq_todos)
        exit()

    list_tasks = rq_todos.json()

    username = rq_user.json().get("username")

    filename = user_id + ".csv"

    with open(filename, 'w') as csvfile:
        for obj in list_tasks:
            row_str = '"{}","{}","{}","{}"\n'.format(
                user_id,
                username,
                obj.get("completed"),
                obj.get("title")
            )
            csvfile.write(row_str)
