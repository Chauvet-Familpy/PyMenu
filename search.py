import googlesearch 
from python_marmiton import Marmiton, RecipeNotFound
from python_septcentcinquanteg import Recipes
from python_cuisineaz import CuisineAZ
from python_cuisinejournaldesfemmes import CuisineJournalDesFemmes
import menudb
import client

user=client.Client().get_id()
def search(arg1, veg=False):
    if veg:
        arg1=+" vegetarien"
        
    recette_list=[]
    
    for i in googlesearch.search("recette"+arg1, tld="co.in", num=20,stop=20, pause=2):
        print(i)
        if(len(recette_list)>3):
            break
            
        if str(i).startswith("https://www.750g.com/"):
            recette_list.append(Recipes.get(str(i)))
            pass

        if str(i).startswith("https://www.cuisineaz.com/recettes/"):
            recette_list.append(CuisineAZ.get(str(i)))
            pass

        if str(i).startswith("https://cuisine.journaldesfemmes.fr/recette/"):
            recette_list.append(CuisineJournalDesFemmes.get(str(i)))
            pass     
        
    #if len(recette_list) < 6:
        #for i in menudb.searchRecipe(menudb.init(), user, arg1, int(veg), 3, 4):
            #recette_list.append(i)
            #if len(recette_list) < 6:
            #    break
            
    return recette_list

print(search("cookies")[3])