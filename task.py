# Classe Task de Panlex App - 2016

import Functions 

class Task:
    
    task_counter = 0
    
    def __init__ (self, creationDate, description, workload, deadline, priority, subtask):  
        self.__idTask = Task.task_counter
        Task.task_counter += 1
        self.__creationDate = creationDate
        self.__description = description
        self.__workload = workload
        self.__deadline = deadline
        self.__priority = priority
        self.__subtask = subtask
        self.__done = 0
        self.__weight = 0
    
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
        
    def set_subtask(self, subtask):
        self.__subtask = subtask
        
    def set_done(self, done):
        self.__done += done  
        
    def set_weight(self):
        self.__weight = (notCompleted(self)/remainingTime(self))*get_priority(self)
        
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
    
    def get_subtask(self):
        return self.__subtask
        
    def get_done(self):
        return self.__done    
    
    def get_weight(self):
        return self.__weight