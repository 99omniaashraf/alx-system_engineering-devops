#!/usr/bin/python3
""" module doc """
import requests
import sys


def main():
    """ def com """
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done = f'{todos}&completed=true'
    notDone = f'{todos}&completed=false'
    userData = requests.get(f'{url}{users}').json()
    Name = userData[0].get("name")
    todosData = requests.get(f'{url}{todos}').json()
    todosDone = requests.get(f'{url}{done}').json()
    doneN = len(todosDone)
    totalN = len(todosData)
    print(f'Employee {Name} is done with tasks({doneN}/{totalN}):')
    for task in todosDone:
        print("\t "+task.get("title"))


if __name__ == "__main__":
    main()
