

# Program to Show how to create a switch  
# import kivy module     
import kivy   
import menudb
from client import *
from kivy.properties import StringProperty
from marmiton import Marmiton, RecipeNotFound
from firebaseloginscreen import FirebaseLoginScreen
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

   
# Create a class for all screens in which you can include 
# helpful methods specific to that screen 
class SearchMenu(Screen): 
    pass
   
class ShowResults(Screen): 
    pass

class MenuGenerator(Screen):
    pass


# Create the App class 
class ScreenApp(App): 
    current_menu_list=[]
    current_menu_names4=StringProperty('')
    current_menu_names3=StringProperty('')
    current_menu_names2=StringProperty('')
    current_menu_names1=StringProperty('')
    current_menu_names0=StringProperty('')
    image0=StringProperty('')
    image1=StringProperty('')
    image2=StringProperty('')
    image3=StringProperty('')
    image4=StringProperty('')
    txtNbPersonnes=StringProperty('Entrez le nombre de personnes')
    txtNbRepas=StringProperty('Entrez le nombre de repas')
    es=menudb.init()
    def build(self): 
        # The ScreenManager controls moving between screens 
        Builder.load_file("main.kv") 
        self.screen_manager = ScreenManager() 
        self.screen_manager.add_widget(FirebaseLoginScreen(name="firebase_login_screen"))
        self.screen_manager.add_widget(SearchMenu(name ="searchmenu")) 
        self.screen_manager.add_widget(ShowResults(name ="showresults"))
        self.screen_manager.add_widget(MenuGenerator(name ="menuGenerator"))
        self.screen_manager.current="firebase_login_screen"

        self.user=Client()
        self.vg=False
        self.textsearch='Empty'
        return self.screen_manager 
    def text(self,g):
        self.textsearch=g 
    def veg(self, hh):
        self.vg=not(self.vg) 
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
        self.screen_manager.current="showresults"
        if len(menu_list)==0:
            while len(self.current_menu_list)<5:
                self.current_menu_list.append({"image":"","name":"Aucuns résultats","url":""})
        else:
            while len(self.current_menu_list)<5:
                self.current_menu_list.append(self.current_menu_list[-1])
        
        self.current_menu_names4=self.current_menu_list[4]["name"]
        self.current_menu_names3=self.current_menu_list[3]["name"]
        self.current_menu_names2=self.current_menu_list[2]["name"]
        self.current_menu_names1=self.current_menu_list[1]["name"]
        self.current_menu_names0=self.current_menu_list[0]["name"]
        
        self.image0=Marmiton.get(self.current_menu_list[0]["url"])["image"]
        self.image1=Marmiton.get(self.current_menu_list[1]["url"])["image"]
        self.image2=Marmiton.get(self.current_menu_list[2]["url"])["image"]
        self.image3=Marmiton.get(self.current_menu_list[3]["url"])["image"]
        self.image4=Marmiton.get(self.current_menu_list[4]["url"])["image"]


        
    def confirmRecipe(self,i):
        menudb.confirmRecipe(self.es, id=self.user.get_id() , recipe=self.current_menu_list[i])




    def getlabel(self, i):
        return self.current_menu_names[i]["name"]
    nbPersonnes=4
    def defnbPersonnes(self,txt):
        try:
            self.nbPersonnes=int(txt)
            self.txtNbPersonnes='Entrez le nombre de personnes'
        except:
            self.txtNbPersonnes='Entrez le nombre de personnes, nombre incorrect !'
    nbRepas=1
    def defnbRepas(self,txt):
        try:
            self.nbRepas=int(txt)
           
            self.txtNbRepas='Entrez le nombre de repas'
        except:
            
            self.txtNbRepas='Entrez le nombre de repas, nombre incorrect !'
    def generateMenu(self):
        pass

# run the app  
sample_app = ScreenApp() 
sample_app.run() 
