from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition

import ScreenPanlex

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


presentation = Builder.load_file("Screen.kv")

class PanlexApp(App):
    def build(self):
        manager = ScreenManager()
        
        manager.add_widget(LoginScreen(name='login'))
        manager.add_widget(SignupScreen(name='signup'))
        manager.add_widget(TaskScreen(name='task'))
        manager.add_widget(SettingsScreen(name='settings'))
        manager.add_widget(NewTaskScreen(name='newtask'))
        manager.add_widget(EditTaskScreen(name='edittask'))
        manager.add_widget(DeleteTaskScreen(name='deletetask'))
        
        return manager


if __name__ == '__main__':
    PanlexApp().run()