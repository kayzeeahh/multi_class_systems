from lib.todo import *
from lib.todo_list import *

"""
Given 2 todos, one complete and one incomplete
it returns the incomplete one
"""
def test_return_incomplete_when_given_complete_and_incomplete():
    todo_list = TodoList()
    todo_1 = Todo("bins")
    todo_2 = Todo("wash the car")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    assert todo_list.incomplete() == [todo_2]
    
"""
Given 2 todos, one complete and one incomplete
it returns the complete one 
"""
def test_return_complete_when_given_complete_and_complete():
    todo_list = TodoList()
    todo_1 = Todo("bins")
    todo_2 = Todo("wash the car")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    assert todo_list.complete() == [todo_1]

"""
Given 2 todos,
none should be incomplete
"""
def test_give_up():
    todo_list = TodoList()
    todo_1 = Todo("bins")
    todo_2 = Todo("wash the car")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.give_up()
    assert todo_list.incomplete() == []
