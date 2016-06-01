class Task:
    
    def __init__ (self, idTask, description, workload, deadline, priority, subtask, creationDate):
        self.__idTask = idTask
        self.__description = description
        self.__workload = workload
        self.__deadline = deadline
        self.__priority = priority
        self.__subtask = subtask
        self.__creationDate = creationDate
        
    # Métodos set
    
    def set_idTask(self, idTask):
        self.__idTask = idTask
        
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
        
    def set_creationDate(self, creationDate):
        self.__creationDate = creationDate
        
    # Métodos get
    
    def get_idTask(self):
        return __idTask
    
    def get_description(self):
        return __description
    
    def get_workload(self):
        return __workload
    
    def get_deadline(self):
        return __deadline
    
    def get_priority(self):
        return __priority
    
    def get_subtask(self):
        return __subtask
    
    def get_creationDate(self):
        return __creationDate
