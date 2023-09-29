from lib.todo import *

"""
iniitialising a task
it creates a todo
"""
def test_initializing_a_task():
    todo = Todo("learn python")
    assert todo.task == "learn python"    
    
"""
When a task is marked as complete
it sets the task as complete
"""
def test_setting_a_task_as_complete():
    todo = Todo("learn python")
    todo.mark_complete()
    assert todo.complete == True