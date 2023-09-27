class TodoList:
    def __init__(self):
        self.todo_list = []
        

    def add(self, todo):
        if type(todo.complete) == bool:
            self.todo_list.append(todo)
        
    
    def incomplete(self):
        return [todo for todo in self.todo_list if todo.complete == False]
        """incompleted_todo = []
        for todo in self.todo_list:
            if todo.complete == False:
                incompleted_todo.append(todo)
        return incompleted_todo"""

    def complete(self):
        return [todo for todo in self.todo_list if todo.complete == True]
        """completed_todo = []
        for todo in self.todo_list:
            if todo.complete == True:
                completed_todo.append(todo)
        return completed_todo"""

    def give_up(self):
        for todo in self.todo_list:
            todo.mark_complete()
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete