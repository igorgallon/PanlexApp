from User import User
from Task import Task
import time
import datetime

user = User('Igor Gallon', 5, 10)
description = 'aiuheiua'
workload = 10
deadline = datetime.datetime.now()
priority = 10
subtask = ''

user.createTask(description, workload, deadline, priority, subtask)

#t = Task(datetime.datetime.now(), 'auhau', 15, datetime.datetime.now(), 10, ' ')