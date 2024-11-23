# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n-s_V6lS3kUslSPAD2HcdTzouxvKhzKY
"""

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, task):

        self.tasks.append({'id': self.next_id, 'task': task})
        print(f"Task '{task}' added successfully with ID: {self.next_id}")
        self.next_id += 1

    def update_task(self, task_id, new_task):

        found = False
        for task in self.tasks:
            if task['id'] == task_id:
                old_task = task['task']
                task['task'] = new_task
                print(f"Task ID {task_id} updated from '{old_task}' to '{new_task}'")
                found = True
                break

        if not found:
            print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):

        found = False
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} ('{task['task']}') deleted successfully.")
                found = True
                break

        if not found:
            print(f"Task ID {task_id} not found.")

    def list_tasks(self):

        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Current Tasks:")
            for task in self.tasks:
                print(f"ID {task['id']}: {task['task']}")

todo_list = ToDoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Read a book")
todo_list.list_tasks()
todo_list.update_task(1, "Buy groceries and cook dinner")
todo_list.delete_task(2)
todo_list.list_tasks()