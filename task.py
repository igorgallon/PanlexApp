''' Classe Tarefa
    idTask: identifica��o da Tarefa
    creationDate: data de cria��o da tarefa (em data)
    description: descri��o da tarefa
    workload: tempo estimado pelo usu�rio para realizar a tarefa (em horas)
    deadline: prazo para conclus�o da tarefa (em data)
    priority: prioridade para realizar a tarefa (1 - menos priorit�rio, 5 - mais priorit�rio)
    subtask: sub-tarefas a serem cumpridas dentro da tarefa
    done: tempo j� conclu�do da tarefa (em horas)
'''

import functions1 

class Task:
    
    def __init__ (self, idTask, creationDate, description, workload, deadline, priority, subtask, done):
        self.__idTask = idTask
        self.__creationDate = creationDate
        self.__description = description
        self.__workload = workload
        self.__deadline = deadline
        self.__priority = priority
        self.__subtask = subtask
        self.__done = done
        self.__weight = weight
        
    # M�todos set
    
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
        self.__done = done  
        
    def set_weight(self, weight):
        self.weight = notCompleted(self)/remainingTime(self)*get_priority(self)
        
    # M�todos get
    
    def get_idTask(self):
        return __idTask

    def get_creationDate(self):
        return __creationDate    
    
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
        
    def get_done(self):
        return __done    
    
    def get_weight(self):
        return __weight