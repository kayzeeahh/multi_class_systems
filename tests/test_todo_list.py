import pytest
from lib.todo_list import *
from lib.todo import *

    
"""
given a todo
it adds to the list
"""
def test_adding_todo_object():
    todo_list = TodoList()
    todo_1 = Todo("learn python")
    todo_list.add(todo_1)
    assert todo_list.todo_list == [todo_1]
