

# Program to Show how to create a switch  
# import kivy module     
import kivy   
import menudb
from client import *
from kivy.properties import StringProperty
from marmiton import Marmiton, RecipeNotFound
from firebaseloginscreen import FirebaseLoginScreen
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  
from random import randint
     
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
class ModifyMenu(Screen):
    pass
class MesRecettes(Screen):
    pass
class MesRecettesDetails(Screen):
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
    detail1=StringProperty('')
    detail4=StringProperty('')
    detail2=StringProperty('')
    detail3=StringProperty('')
    def build(self):
        Builder.load_file("main.kv") 
        self.user_localId = -1
    
        self.screen_manager = ScreenManager() 
        self.screen_manager.add_widget(FirebaseLoginScreen(name="firebase_login_screen"))
        self.screen_manager.add_widget(SearchMenu(name ="searchmenu")) 
        self.screen_manager.add_widget(ShowResults(name ="showresults"))
        self.mes_recettes_detail=MesRecettesDetails(name="mes_recettes_detail")
        self.screen_manager.add_widget(self.mes_recettes_detail)
        self.mes_recettes=MesRecettes(name ="mes_recettes")
        self.screen_manager.add_widget(self.mes_recettes)
        self.modify_menu=ModifyMenu(name ="modifymenu")
        self.screen_manager.add_widget(self.modify_menu)
        self.menu_generator=MenuGenerator(name ="menuGenerator")
        self.screen_manager.add_widget(self.menu_generator)
        self.screen_manager.current="firebase_login_screen"

        
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
        menu_list = menudb.searchRecipe(menudb.init(), self.user.get_id(), self.textsearch,  self.exp_last_press, self.dif_last_press,veg=self.vg)
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
        
        self.image0=self.current_menu_list[0]["image"]
        self.image1=self.current_menu_list[1]["image"]
        self.image2=self.current_menu_list[2]["image"]
        self.image3=self.current_menu_list[3]["image"]
        self.image4=self.current_menu_list[4]["image"]


        
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
    def delete_recipe(self,btn):
        menudb.delMenu(self.es, self.user.get_id(),self.last_my_recipe_pressed)
        self.populate_mes_recettes()


    def show_details(self,btn):
        self.screen_manager.current="mes_recettes_detail"
        self.last_my_recipe_pressed=btn.nb
        self.detail1=self.res["menuList"][btn.nb]["image"]
        self.detail2=self.res["menuList"][btn.nb]["name"]
        self.detail3=str(self.res["menuList"][btn.nb]["ingredients"])
        self.detail4=str(self.res["menuList"][btn.nb]["step"])
        


    def populate_mes_recettes(self):
        res=self.es.get(index='users',id=self.user.get_id())
        self.res=res['_source']
        grid=self.mes_recettes.ids['my_recipe_grid']
        grid.clear_widgets()
        for i in range(len(self.res["menuList"])):
            btn=Button(text=self.res["menuList"][i]["name"],on_release=self.show_details)
            btn.nb=i
            grid.add_widget(btn)

    def change_recipe(self,btn):#Probablement a supprimer
        self.imageMenu[btn.nb]=self.res["menuList"][btn.new_recipe]["image"]
        self.nameMenu[btn.nb]=self.res["menuList"][btn.new_recipe]["name"]
        self.res["menuCreated"][-1][btn.nb]=self.res["menuList"][btn.new_recipe]
        self.screen_manager.current='menuGenerator'
        
        self.box_menu.clear_widgets()
        self.imageMenu=[]
        self.nameMenu=[]
        for i in range(len(self.res["menuCreated"][-1])):
            new=GridLayout(cols=3,rows=1,spacing=10)
            l=Label(size_hint=(1,.03), text="repas n°"+str(i+1),size_hint_y=None)
            self.box_menu.add_widget(l)
            self.imageMenu.append(self.res["menuCreated"][-1][i]["image"])
            
            ai=AsyncImage(size_hint=(1/3,.2), source=self.imageMenu[-1],size_hint_y=None)
            new.add_widget(ai)
            
            self.nameMenu.append(self.res["menuCreated"][-1][i]["name"])
            l=Label(size_hint=(1/3,.2), text=self.nameMenu[-1],size_hint_y=None)
            new.add_widget(l)
            btn=Button(size_hint=(1/3,.2), text="modifier repas "+str(i+1),size_hint_y=None,on_release=self.modifier_menu)
            btn.nb=i
            ai.id="ai_menu"+str(i)
            l.id="l_menu"+str(i)
            btn.recipe=i
            new.add_widget(btn)
            self.box_menu.add_widget(new)
        self.es.index(index="users",id=self.user.get_id(),body=self.res)
            
        print("populated boxlayout")
        

    
        

    def modifier_menu(self,btn):
        self.screen_manager.current="modifymenu"
        box_modify=self.modify_menu.ids["grid_modify"]
        box_modify.clear_widgets()
        
        
        for i in range(len(self.res["menuList"])):
            bt=Button(text=self.res["menuList"][i]["name"],on_release=self.change_recipe)
            bt.nb=btn.nb
            bt.new_recipe=i
            box_modify.add_widget(bt)




    def generateMenu(self):
        self.box_menu=self.menu_generator.ids["box_menu"]
        self.box_menu.clear_widgets()
        res=self.es.get(index='users',id=self.user.get_id())
        self.res=res['_source']
        self.res['menuCreated'].append([])
        #res['menuCreated'].append([])
        self.imageMenu=[]
        self.nameMenu=[]
        for i in range(self.nbRepas):
            new=GridLayout(cols=3,rows=1,spacing=10)
            j=randint(0,len(self.res["menuList"])-1)
            self.res['menuCreated'][-1].append(self.res['menuList'][j])
            l=Label(size_hint=(1,.03), text="repas n°"+str(i+1),size_hint_y=None)
            self.box_menu.add_widget(l)
            self.imageMenu.append(self.res["menuList"][j]["image"])
            
            ai=AsyncImage(size_hint=(1/3,.2), source=self.imageMenu[-1],size_hint_y=None)
            new.add_widget(ai)
            
            self.nameMenu.append(self.res["menuList"][j]["name"])
            l=Label(size_hint=(1/3,.2), text=self.nameMenu[-1],size_hint_y=None)
            new.add_widget(l)
            btn=Button(size_hint=(1/3,.2), text="modifier repas "+str(i+1),size_hint_y=None,on_release=self.modifier_menu)
            btn.nb=i
            ai.id="ai_menu"+str(j)
            l.id="l_menu"+str(j)
            btn.recipe=j
            new.add_widget(btn)
            self.box_menu.add_widget(new)
        self.es.index(index="users",id=self.user.get_id(),body=self.res)
        print("populated boxlayout")

    def search_insaved_recipe(self,text):
        if text=="":
            self.res=self.es.get(id=self.user.get_id(),index="users")
            return self.res["_source"]["menuList"]
        else:
            query={
                "query": {
                    "match": {
                    "_id": "elasticsearch" 
                    }
                }
            }
            self.res=self.es.search(index=users,body=query)
    
    def search_in_modify_menu(self,text):
        pass


    



sample_app = ScreenApp() 
sample_app.run() 
