# Classe Panlex de Panlex App - 2016
# Gerenciador da interface grafica

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition

class SeeTasksScreen(Screen):
    # Devera exibir todas as tasks que o usuario possui
    pass

class TaskScreen(Screen):
    pass

class SettingsScreen(Screen):
    # Devera fornecer a escolha dos intens:
    #   - Workload diario;
    #   - Quantidade de tasks por dia;
    #   - Nome do Usuario.
    pass

class NewTaskScreen(Screen):
    def on_event(self,obj):
            print("Typical event from " + obj)
            print(self.ids)
            
            # Id precisa ser algumacoisa _ alguma coisa
            
            texto = self.ids["id_text"]
            print(texto.text)
            
class EditTaskScreen(Screen):
    # Devera ser possivel editar as especificacoes de uma task dentre uma lista, como:
    #    - Nome;
    #    - Workload;
    #    - Deadline;
    #    - Prioridade;
    #    - Descricao;
    #    - Excluir task.
    pass

presentation = Builder.load_file("ScreensPanlex.kv")

class PanlexApp(App):
    def build(self):
        manager = ScreenManager()
        
        manager.add_widget(TaskScreen(name='task'))
        manager.add_widget(SettingsScreen(name='settings'))
        manager.add_widget(NewTaskScreen(name='newtask'))
        manager.add_widget(EditTaskScreen(name='edittask'))
        manager.add_widget(SeeTasksScreen(name='seetasks'))
        
        return manager


if __name__ == '__main__':
    PanlexApp().run()