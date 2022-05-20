#!/usr/bin/python3
"""
export data in the CSV format.
"""
import json
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

    filename = user_id + ".json"

    new_list = []
    with open(filename, 'w') as jfile:
        for obj in list_tasks:
            tmp_dict = {}
            tmp_dict["task"] = obj.get("title")
            tmp_dict["completed"] = obj.get("completed")
            tmp_dict["username"] = username
            new_list.append(tmp_dict)

        dict_to_save = {user_id: new_list}
        jfile.write(json.dumps(dict_to_save))
