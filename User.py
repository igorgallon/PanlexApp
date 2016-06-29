from DB import DB

class User:
    def __init__ (self, username, numTasksDaily, workloadDaily):
        self.__username = username
        self.__numTasksDaily = numTasksDaily
        self.__workloadDaily = workloadDaily
    
    # --- Metodos set ---
    
    def set_username(self, username):
        self.__username = username
        DB.insertUserSettings(self, self.__username, self.__numTasksDaily, self.__workloadDaily)
        
    def set_numTasksDaily(self, numTaksDaily):
        self.__numTasksDaily = numTasksDaily
        DB.insertUserSettings(self, self.__username, self.__numTasksDaily, self.__workloadDaily)
    
    def set_workloadDaily(self, workloadDaily):
        self.__workloadDaily = workloadDaily
        DB.insertUserSettings(self, self.__username, self.__numTasksDaily, self.__workloadDaily)
        
    # --- Metodos get ---
    
    def get_username(self):
        return self.__username
    
    def get_numTasksDaily(self):
        return self.__numTasksDaily
    
    def get_workloadDaily(self):
        return self.__workloadDaily
    
    # Obtem informacoes de User
    def get_info(self):
        print (self.__username, self.__numTasksDaily, self.__workloadDaily)
    
    # Atualiza informacoes de User
    def set_info(self, username, numTasksDaily, workloadDaily):
        User.set_username(self, username)
        User.set_numTasksDaily(self, numTasksDaily)
        User.set_workloadDaily(self, workloadDaily)