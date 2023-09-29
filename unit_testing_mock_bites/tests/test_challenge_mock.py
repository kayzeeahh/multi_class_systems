from unittest.mock import *

def test_creates_a_sophisticated_mock():
    # Uncomment and set up your mocks here
    task_list = Mock()
    task = "Learn Python"
    task_list.add.return_value = task
    task_list.list.return_value = [task]
    task_list.count.return_value = 1
    task_list.clear.return_value = "success"

    # Don't edit below
    task_list.add(task)
    assert task_list.list() == [task]
    assert task_list.count() == 1
    assert task_list.clear() == "success"
    
def test_for_mock_was_called():
    task_list = Mock()
    
    task = "Learn Python"
    task_list.add.return_value = task
    task_list.list.return_value = [task]
    task_list.count.return_value = 1
    task_list.clear.return_value = "success"
    
    assert task_list.add(task) == task
    
    task_list.add.assert_called()
    task_list.add.assert_called_with(task)
    
    
    
    

