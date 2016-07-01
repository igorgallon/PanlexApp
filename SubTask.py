# Classe de SubTasks de PanlexApp 2016

class SubTask:

    def __init__ (self, idTask, description, done):
        self.__idTask = idTask
        self.__description = description
        self.__done = done
        
    # --- Metodos set ---

    def set_idTask(self, idTask):
        self.__idTask = idTask
    
    def set_idSubTask(self, idSubTask):
        self.__idSubTask = idSubTask    
        
    def set_description(self, description):
        self.__description = description
        
    def set_done(self, done):
        self.__done = done
  
    # --- Metodos get ---
    
    def get_idTask(self):
        return self.__idTask 
    
    def get_idSubTask(self):
        return self.__idSubTask

    def get_description(self):
        return self.__description

    def get_done(self):
        return self.__done
    
    # Atualiza informacoes de SubTask
    def set_info(self, idTask, description, done):
        SubTask.set_idTask(self, idTask)
        SubTask.set_description(self, description)
        SubTask.set_done(self, done)
        
    # Retorna informacoes de SubTask
    def get_info(self):
        print (self.__idTask, self.__idSubTask, self.__description, self.__done)