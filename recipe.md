{{PROBLEM}} Multi-Class Planned Design Recipe
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
>As a user
>So that I can keep track of my tasks
>I want a program that can add todo tasks to and see a list of them

>As a user 
>So that I can focus on tasks to complete
>I want to mark tasks as complere and have them disappear from the list

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

#Nouns (things the user will interact with)
task
list of tasks
program


#Verbs (operations the user will perform)
add 
see a list
marking something complete
disappear


  ┌───────────────────────────┐
  │        Task list:         │
  │                           │
  │                           │
  │ add(track)                │
  │                           │
  │ list(incomplete)          │
  │                           │
  │ list(complete)            │
  │                           │
  └─────────────┬─────────────┘
                │
                │
   ┌────────────▼─────────────┐
   │                          │
   │                          │
   │            Task          │
   │    Title [property]      │
   │   Initialise(title)      │
   │                          │
   │   mark_complete()        │
   │                          │
   │   complete [property]    │
   │                          │
   └──────────────────────────┘

class TaskTracker:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
class Task:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

"""
When I add multiple tasks
They come back in the incomplete list
"""
tracker = TaskTracker()
task_1 = Task("Walk the dog")
task_2 = Task("Clean the car")
tracker.add(task_1)
tracker.add(task_2)
tracker.list_complete() == [task_1, task_2]


"""
When I add multiple tasks
And mark one as complete
It does not show up in the incomplete list anymore
"""
tracker =Tracker()
task_1 = Task("Walk the dog")
task_2 = Task("Clean the car")
tracker.add(task_1)
tracker.add(task_2)
task_1.mark_complete()
tracker.list_incomplete() = [task_2]


"""
When I add multiple tasks
And mark one as complete
It shows up in the complete list 
"""
tracker =Tracker()
task_1 = Task("Walk the dog")
task_2 = Task("Clean the car")
tracker.add(task_1)
tracker.add(task_2)
task_1.mark_complete()
tracker.list_complete() = [task_1]

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

#TaskTracker unit tesst
"""
Initially, the incomplete task list is empty
"""
tracker = TaskTracker()
tracker.list_incomplete = []

"""
Initially, the complete task list is empty
"""
tracker = TaskTracker()
tracker.list_complete = []


#Tasks unit tests
"""
When we create a task 
it apprears in the task function
"""
task = Task("Walk the dog.)
task.title = "Walk the dog.

"""
When we create a task 
it is initially incomplete
"""
task = Task("Walk the dog.")
task.complete = False

When we create a task 
and mark it complete
it is in the complete list
"""
task = Task("Walk the dog.")
task.mark_complete()
task.complete = True


5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
























{{PROBLEM}} Multi-Class Planned Design Recipe
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
>As a user
>So that I can record my experiences
>I want to keep a regular diary

>As a user
>So that I can reflect on my experiences
>I want to read my past diary entries

>As a user
>So that I can reflect on my experiences in my busy day
>I want to select diary entries to read based on how much time I have and my reading speed

>As a user
>So that I can keep track of my tasks
>I want to keep a todo list along with my diary

>As a user
>So that I can keep track of my contacts
>I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

#Nouns (things the user will interact with)
diary
diary entries
experiences
time
reading speed
todo list
tasks
phone numbers
list of phone numbers


#Verbs (operations the user will perform)
Record
keep
reflect
read
select
keep
see a list
mark complete
list complete
list incomplete
add


  
   ┌───────────────────────────┐
   │        DiaryEntry         │
   │                           │
   │  add(diary entry)         │
   │  read(diary entry)        │
   │  reading time(mins, wpm)  │
   │                           │
   │                           │
   │                           │
   │                           │
   └─────────────┬─────────────┘
                 │
                 │
                 │
                 │
   ┌─────────────▼───────────────┐
   │                             │
   │      Tracker                │
   │                             │
   │  todo(list of todo)         │
   │  contact_list(name, number) │
   │                             │
   └─────────────────────────────┘


class Diary:
    def add(self, entry):
        # entry: instance of DiaryEntry
        # returns nothing
        # adds a list of diary entries

    def all(self):
        # returns a list of DiaryEntry instances
        pass    
class DiaryEntry():
    def ___init__(self, title, contents)
    
class TaskList()
    def add(self, task):
        
    def all_incomplete(self):

    def all_complete(self):

class Task():
    def __init__(self, title):

    def extract(self):

class PhoneNumberExtraction():
    def extract(self, diary):


class ReadableEntryExtractor():
    def __init__(self, diary):

    def extract(self, wpm, minutes)


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

"""
When I add multiple diary entries
#all lists them out in the order they were added
"""
diary = Diary()
entry_1 = DiaryEntry("My title 1", "My Contents 1")
entry_2 = DiaryEntry("My title 1", "My Contents 1")
entry_3 = DiaryEntry("My title 1", "My Contents 1")
entry_4 = DiaryEntry("My title 1", "My Contents 1")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.add(entry_4)
diary.all() == [entry_1,entry_2,entry_3,entry_4,]

"""
When I add multiple
And I dont mark any complete
#all_incomplete lists them out 
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the rabbit")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_list.incomplete == [task_1, task_2, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_incomplete only lists the incomplete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the rabbit")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.incomplete == [task_1, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_complete only lists the complete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the rabbit")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.complete == [task_2]

"""
When I add multiple diary entries
and I call PhoneNumberExtractor #extract
I get a list of phone numbers from all diary entries
"""
diary = Diary()
entry_1 = DiaryEntry("My title 1", "My phone number is 07800000000 and 07800000001")
entry_2 = DiaryEntry("My title 1", "My Contents 1")
entry_2 = DiaryEntry("My title 1", "My phone number is 07800000002")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = PhoneNumberExtractor(diary)
extractor.extract() == ["07800000000", "07800000001", "07800000002"]


4. Create Examples as Unit Tests

Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

#Diary unit test
"""
Initially, Diary has no entries
"""
diary = Diary()
diary.all == []

"""
Initially, the complete task list is empty
"""
diary = Diary()
diary.all == []

#DiaryEntry unit tests
"""
DiaryEntry is constructed with a title and contents
"""
entry = DiaryEnrty(:My Title", "My contents")
entry.title == "My Title
entry.contents == "My contents

#TaskList unit tests
"""
Initially TrackList has no incomplete tasks
"""
track_list = TrackList()
tracklist.all_incomplete == []

"""
Initially TrackList has no complete tasks
"""
track_list = TrackList()
tracklist.all_complete == []

#Task unit test
"""
Task contracts with a title
"""
task = Task("Walk the dog")
task.title == "Walk the dog"



#PhoneNumberExtraction unit tests




#ReadableEntryFinder unit tests

5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.