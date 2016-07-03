from DB import DB

class User:

    def __init__(self, username, numTasksDaily, workloadDaily):
        self.__username = username
        self.__numTasksDaily = numTasksDaily
        self.__workloadDaily = workloadDaily
        self.__idSubTask = 0

    # --- Metodos set ---
    
    def set_username(self, username):
        db = DB()
        self.__username = username
        db.insertUserSettings(self.__username, self.__numTasksDaily, self.__workloadDaily)
        
    def set_numTasksDaily(self, numTasksDaily):
        db = DB()
        self.__numTasksDaily = numTasksDaily
        db.insertUserSettings(self.__username, self.__numTasksDaily, self.__workloadDaily)
    
    def set_workloadDaily(self, workloadDaily):
        db = DB()
        self.__workloadDaily = workloadDaily
        db.insertUserSettings(self.__username, self.__numTasksDaily, self.__workloadDaily)
        
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
        self.set_username(username)
        self.set_numTasksDaily(numTasksDaily)
        self.set_workloadDaily(workloadDaily)