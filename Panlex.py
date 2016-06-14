from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""

<LoginScreen>:
    BoxLayout:
        Button:
            text: 'Cadastrar usuário'
            on_press: root.manager.current = 'signup'
        Button:
            text: 'Entrar'
            on_press: root.manager.current = 'task'
        Button:
            text: 'Sair'
            on_press: App.get_running_app().stop()

<SignupScreen>:
    BoxLayout:
        Button:
            text: 'OK'
            on_press: root.manager.current = 'login'
        Button:
            text: 'Voltar'
            on_press: root.manager.current = 'login'
            
<TaskScreen>:
    BoxLayout:
        Button:
            text: 'Adicionar Tarefas'
            on_press: root.manager.current = 'newtask'
        Button:
            text: 'Editar Tarefas'
            on_press: root.manager.current = 'edittask'
        Button:
            text: 'Excluir Tarefas'
            on_press: root.manager.current = 'deletetask'                
        Button:
            text: 'Configurações'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Sair'
            on_press: root.manager.current = 'login'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'OK'
            on_press: root.manager.current = 'task' 
        Button:
            text: 'Cancelar'
            on_press: root.manager.current = 'task'

<NewTaskScreen>:
    BoxLayout:
        Button:
            text: 'OK'
            on_press: root.manager.current = 'task'
        Button:
            text: 'Cancelar'
            on_press: root.manager.current = 'task'
            
<EditTaskScreen>:
    BoxLayout:
        Button:
            text: 'OK'
            on_press: root.manager.current = 'task'
        Button:
            text: 'Cancelar'
            on_press: root.manager.current = 'task'
            
<DeleteTaskScreen>:
    BoxLayout:
        Button:
            text: 'OK'
            on_press: root.manager.current = 'task'
        Button:
            text: 'Cancelar'
            on_press: root.manager.current = 'task'  
""")

# Declare both screens
class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class TaskScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class NewTaskScreen(Screen):
    pass

class EditTaskScreen(Screen):
    pass

class DeleteTaskScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(TaskScreen(name='task'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(NewTaskScreen(name='newtask'))
sm.add_widget(EditTaskScreen(name='edittask'))
sm.add_widget(DeleteTaskScreen(name='deletetask'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()