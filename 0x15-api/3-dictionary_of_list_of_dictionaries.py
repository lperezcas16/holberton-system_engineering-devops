#!/usr/bin/python3
"""
export data in the CSV format.
"""
import json
import requests


filename = "todo_all_employees.json"

url = "https://jsonplaceholder.typicode.com/users/"
rq_users = requests.get(url=url)

list_users = rq_users.json()

if rq_users.status_code >= 300:
        print(rq_users)
        exit()

dict_to_save = {}

for obj in list_users:
    new_list = []
    user_id = str(obj.get("id"))
    username = obj.get("username")

    url = "https://jsonplaceholder.typicode.com/users/" + user_id + "/todos"
    rq_todos = requests.get(url=url)

    if rq_todos.status_code >= 300:
        print(rq_todos)
        exit()

    list_tasks = rq_todos.json()

    for obj in list_tasks:
        tmp_dict = {}
        tmp_dict["completed"] = obj.get("completed")
        tmp_dict["task"] = obj.get("title")
        tmp_dict["username"] = username
        new_list.append(tmp_dict)

    dict_to_save[user_id] = new_list

with open(filename, 'w') as jfile:
    jfile.write(json.dumps(dict_to_save))
