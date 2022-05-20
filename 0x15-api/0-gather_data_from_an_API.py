#!/usr/bin/python3
"""
This script using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
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

    EMPLOYEE_NAME = rq_user.json().get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(list_tasks)

    list_complete = []

    for obj in list_tasks:
        if obj.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            list_complete.append(obj)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS
        )
    )

    for obj in list_complete:
        print("\t " + obj.get("title"))
