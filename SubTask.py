# Classe de SubTasks de PanlexApp 2016

class SubTask:
    
    subtask_counter = 0
       
    def __init__ (self, description, done):  
        self.__idSubTask = SubTask.subtask_counter
        SubTask.subtask_counter += 1      
        self.__description = description
        self.__done = done
        
    # --- Metodos set ---

    def set_description(self, description):
        self.__description = description
        
    def set_done(self, done):
        self.__done = done
  
    # --- Metodos get ---
    
    def get_idSubTask(self):
        return self.__idSubTask

    def get_description(self):
        return self.__description

    def get_done(self):
        return self.__done
    
    # Atualiza informacoes de SubTask
    def set_info(self, description, done):
        SubTask.set_description(self, description)
        SubTask.set_done(self, done)
        
    # Retorna informacoes de SubTask
    def get_info(self):
        print (self.__idSubTask, self.__description, self.__done)