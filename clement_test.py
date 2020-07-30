

# Program to Show how to create a switch  
# import kivy module     
import kivy   
import menudb
from client import *
       
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  
     
# this restrict the kivy version i.e   
# below this kivy version you cannot   
# use the app or software   
kivy.require('1.9.0') 
  
# Builder is used when .kv file is 
# to be used in .py file 
from kivy.lang import Builder 
  
# The screen manager is a widget 
# dedicated to managing multiple screens for your application. 
from kivy.uix.screenmanager import ScreenManager, Screen 
   
# You can create your kv code in the Python file 
Builder.load_file("clement_test.kv") 
   
# Create a class for all screens in which you can include 
# helpful methods specific to that screen 
class SearchMenu(Screen): 
    pass
   
class ShowResults(Screen): 
    pass
  
   
# The ScreenManager controls moving between screens 
screen_manager = ScreenManager() 
   
# Add the screens to the manager and then supply a name 
# that is used to switch screens 
screen_manager.add_widget(SearchMenu(name ="searchmenu")) 
screen_manager.add_widget(ShowResults(name ="showresults")) 

  
# Create the App class 
class ScreenApp(App): 
    
    def build(self): 
        self.user=Client()
        self.vg=False
        self.textsearch='Empty'
        return screen_manager 
    def text(self,g):
        self.textsearch=g 
    def vg(self, hh):
        vg=not(vg) 
    dif_last_press=3   
    def dif_last_pressed(self, event):
        self.dif_last_press = int(event[0].text)
        print(self.dif_last_press)
        
    exp_last_press=4   
    def exp_last_pressed(self, event):
        self.exp_last_press = int(event[0].text)
        print(self.exp_last_press)
    def search(self, hh):
        print("searching")
        menu_list = menudb.searchRecipe(menudb.init(), self.user.get_id(), self.textsearch, vg=self.vg, exp=self.exp_last_press, dif=self.dif_last_press)
        print(menu_list)
        self.current_menu_list=menu_list
        
        screen_manager.current="showresults"
    def getlabel(i):
        return self.current_menu_list[i]
# run the app  
sample_app = ScreenApp() 
sample_app.run() 
