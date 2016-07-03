# Classe Panlex de Panlex App - 2016
# Gerenciador da interface grafica

from Controller2 import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty

class InitialScreen(Screen):
    # Tela inicial do aplicativo
    pass

class SeeTasksScreen(Screen):
    # Lista todas as Tasks que o usuario possui
    pass

class TaskInfoScreen(Screen):
    # Exibe informacoes de uma Task
    pass

class EditTaskScreen(Screen):
    # Edita as especificacoes de uma Task
    #    - Workload;
    #    - Deadline;
    #    - Prioridade;
    #    - Descricao;
    #    - Excluir task.
    pass

class NewTaskScreen(Screen):
    # Cria task
    # - Description
    # - Workload
    # - Deadline
    # - Priority
    def on_event(self,obj):
            print("Typical event from " + obj)
            print(self.ids)
            
            # Id precisa ser algumacoisa _ alguma coisa
            
            texto = self.ids["id_text"]
            print(texto.text)
            
class SettingsScreen(Screen):
    # Exibe informaçoes atuais do usuario:
    # - Username
    # - Workload daily
    # - Number of daily tasks
    username = StringProperty()
    workload = StringProperty()
    numtasks = StringProperty()
    
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        if len(userlist) != 0:
            self.username = userList[0].get_username()
            self.workload = str(userList[0].get_workloadDaily())
            self.numtasks = str(userList[0].get_numTasksDaily())
        else:
            self.username = 'None'
            self.workload = 'None'
            self.numtasks = 'None'
        
class EditSettingsScreen(Screen):
    # Editar informacoes de usuario:
    # - Username
    # - Workload daily
    # - Number of daily Tasks
    username = StringProperty()
    workload = StringProperty()
    numtasks = StringProperty()
    
    user = ctr.get_users()
    
    def __init__(self, **kwargs):
        super(EditSettingsScreen, self).__init__(**kwargs)
        
        if len(userList) != 0:
            self.username = userList[0].get_username()
            self.workload = str(userList[0].get_workloadDaily())
            self.numtasks = str(userList[0].get_numTasksDaily())
        else:
            self.username = 'None'
            self.workload = 'None'
            self.numtasks = 'None'
            
    def ok_button(self):
        username = self.ids['id_username'].text
        workload = int(self.ids['id_workload'].text)
        numtasks = int(self.ids['id_numtasks'].text)
        
        if len(userList) != 0:
            userList[0].set_username(username)
            userList[0].set_workloadDaily(workload)
            userList[0].set_numTasksDaily(numtasks)
        else:
            ctr.createUser(username, numtasks, workload)
        
class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("ScreensPanlex.kv")

class PanlexApp(App):
        
    def build(self):
        return presentation

if __name__ == '__main__':
    PanlexApp().run()