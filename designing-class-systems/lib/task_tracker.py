'''
We want a task_tracker which holds our todos
'''
class TaskTracker():
    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task_list.append(task)

class Task():
    def __init__(self, task):
        self.task = task
        self.done = False

    def complete(self):
        self.done = True