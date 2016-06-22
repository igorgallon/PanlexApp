# Classe Task de Panlex App - 2016

import time
import datetime
import Functions 

class Task:
    
    task_counter = 0
    
    def __init__ (self, description, workload, deadline, priority):  
        self.__idTask = Task.task_counter
        Task.task_counter += 1      
        self.__creationDate = datetime.datetime.now() # Define horario de criacao da Task
        self.__description = description
        self.__workload = workload
        self.__deadline = deadline
        self.__priority = priority
        self.__done = 0
        self.__weight = (Functions.notCompleted(self)/Functions.remainingTime(self))*self.__priority
    
    def get_info(self):
        print (self.__idTask, self.__creationDate, self.__description, self.__workload, self.__deadline, self.__priority, self.__subtask, self.__done, self.__weight)
    
    # Metodos set
    
    def set_idTask(self, idTask):
        self.__idTask = idTask

    def set_creationDate(self, creationDate):
        self.__creationDate = creationDate
    
    def set_description(self, description):
        self.__description = description
        
    def set_workload(self, workload):
        self.__workload = workload
        
    def set_deadline(self, deadline):
        self.__deadline = deadline
        
    def set_priority(self, priority):
        self.__priority = priority
        
    def set_done(self, done):
        self.__done += done  
        
    def set_weight(self):
        # weight = (notCompleted / remainingTime) * priority
        self.__weight = (Functions.notCompleted(self)/Functions.remainingTime(self))*self.__priority
        
    # Metodos get
    
    def get_idTask(self):
        return self.__idTask

    def get_creationDate(self):
        return self.__creationDate    
    
    def get_description(self):
        return self.__description
    
    def get_workload(self):
        return self.__workload
    
    def get_deadline(self):
        return self.__deadline
    
    def get_priority(self):
        return self.__priority

    def get_done(self):
        return self.__done    
    
    def get_weight(self):
        return self.__weight