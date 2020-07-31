from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.button import Button

from client import * 
import menudb

user=Client()

class MainApp(GridLayout):
    
    def __init__(self, **kwargs):
        self.sm = ScreenManager()
        screen = Screen(name='searchMenu')
        self.sm.add_widget(screen)
        super(MainApp, self).__init__(**kwargs)
        self.clearcolor = (1, 1, 1, 1)
        
        self.cols=1
        
        self.add_widget(Label(text="recherche"))
        self.search_entry=TextInput()
        self.add_widget(self.search_entry)
        
        self.add_widget(Label(text="VG"))
        self.search_veg_checkbox=CheckBox(active=False)
        self.add_widget(self.search_veg_checkbox)
        
        self.add_widget(Label(text="Prix"))
        self.exp_btn1 = ToggleButton(text='1', group='exp', on_press=self.exp_last_pressed)
        self.exp_btn2 = ToggleButton(text='2', group='exp', on_press=self.exp_last_pressed)
        self.exp_btn3 = ToggleButton(text='3', group='exp', on_press=self.exp_last_pressed)
        self.exp_btn4 = ToggleButton(text='4', group='exp',  state='down', on_press=self.exp_last_pressed)
        self.add_widget(self.exp_btn1)
        self.add_widget(self.exp_btn2)
        self.add_widget(self.exp_btn3)
        self.add_widget(self.exp_btn4)
        
        self.add_widget(Label(text="Difficuté"))
        self.dif_btn1 = ToggleButton(text='1', group='dif', on_press=self.dif_last_pressed)
        self.dif_btn2 = ToggleButton(text='2', group='dif', on_press=self.dif_last_pressed)
        self.dif_btn3 = ToggleButton(text='3', group='dif',  state='down', on_press=self.dif_last_pressed)
        self.add_widget(self.dif_btn1)
        self.add_widget(self.dif_btn2)
        self.add_widget(self.dif_btn3)
        self.dif_btn1.text
        self.dif_var=ToggleButton.get_widgets("dif")
        
        self.search_button=Button(text="Recherche")
        self.search_button.bind(on_press=self.search)
        self.add_widget(self.search_button)
    
    dif_last_press=3   
    def dif_last_pressed(self, event):
        self.dif_last_press = int(event.text)
        print(self.dif_last_press)
        
    exp_last_press=4   
    def exp_last_pressed(self, event):
        self.exp_last_press = int(event.text)
        print(self.exp_last_press)
        
    def search(self, hh):
        print("searching")
        menu_list = menudb.searchRecipe(menudb.init(), user.get_id(), self.search_entry.text, vg=int(self.search_veg_checkbox.active), exp=self.exp_last_press, dif=self.dif_last_press)
        print(menu_list)
        #research_app.Application(self.search_entry.text, menu_list)
        #self.quit()
        
    def var_setter(self, var, value):
        var=value
        print(var)
        
class MyApp(App):
    def build(self):
        return MainApp()
        
        
if __name__ == "__main__":
    MyApp().run()