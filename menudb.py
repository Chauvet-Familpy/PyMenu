import os, base64, re, logging
from elasticsearch import Elasticsearch
from marmiton import Marmiton, RecipeNotFound
from random import randint

def init():
    es_header = [{
    'host': "pymenu-9375012304.eu-central-1.bonsaisearch.net",
    'port': "443",
    'use_ssl': True,
    'http_auth': ("8u2oau67ax","rlrffxphm0")
    }]

    # Instantiate the new Elasticsearch connection:
    es = Elasticsearch(es_header)

    # Verify that Python can talk to Bonsai (optional):
    return es

def searchRecipe(es, id, name,vg=-1,exp=-1,dif=-1):
    
    res = es.get(index="users", id=0)
    res= res["_source"]
    if exp==-1:
        exp=res["expMax"]
    if dif==-1:
        dif=res["difMax"]
    if vg==-1:
        vg=res["vg"]
    result=[]
    query_options = {
    "aqt": name,  # Query keywords - separated by a white space
    "exp": exp,                    # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
    "dif": dif,                    # Recipe difficulty : 1 -> Very easy, 2 -> Easy, 3 -> Medium, 4 -> Advanced (optional)
    "veg": vg,                    # Vegetarien only : 0 -> False, 1 -> True (optional)
    }
    query_result = Marmiton.search(query_options)
    k=0
    while k<len(query_result):
        try:
            Marmiton.get( query_result[k]['url'])
            k+=1
        except:
            query_result.pop(k)
    l=0
    while(l<len(query_result) and l<5):
        result.append(query_result[l])
        l+=1

    
    return result
    


def confirmRecipe(es, id=0 , recipe="test"):
    
    detailed_recipe = Marmiton.get( recipe['url'])
    res = es.get(index="users", id=id)
    doc=res["_source"]
    ingredients=detailed_recipe["ingredients"]
    for j in range(len(ingredients)):
        i=0
        while(1):
            if ingredients[j][i] in ["1","2","3",'4','5','6','7','8','9','0']:
                i+=1
            else:
                break
        
        if i>0:
            nb=int(ingredients[j][:i])
            nb=nb/float(detailed_recipe["people_quantity"])
            ingredients[j] = str(nb)+ingredients[j][i:]     
            
    doc["menuList"].append({"url":recipe["url"],"name":recipe["name"],"ingredients":ingredients,"step":detailed_recipe['steps']}) 
    es.index(index="users",id=id,body=doc)

def randomMenu(es,id=0):
    res=es.get(index="users", id=id)
    res=res['_source']
    if len(res["menuList"])==0:
        return "erreur bro"
    nb=randint(0,len(res["menuList"])-1)
    return Marmiton.get(res["menuList"][nb]['url'])
    
def delMenu(es,id=0,recipe=0):
    res=es.get(index="users", id=id)
    res=res['_source']
    res["menuList"].pop(recipe)
    es.index(index="users",id=id,body=doc)

def magicButton():
    l=["champigons farcis","endive au four","soupe de potiron","frite / cordon bleu","pizza","croque monsieur","ravioli","crèpes sucrée","pâtes carbonara","coquiette bolognaise","endive poelée au lardon","pomme de terre farcie","frites steak hache ou omelette","pomme de terre avec oignon carrote et viande au choix a la poele","hachis parmentier","tagliatelle avec escalope a la crème et au champignon","gratin de pomme de terre et choux fleur","tourte","tarte au maroile","flamenkusch","tomate farcie","poulet rôti avec des chips","gâteau salé ","quiche loraine","lasagne","poulet en cocotte avec pomme de terre oignon carotte champignonchoucroute","palette a la diable","potée","riz roulé dans du jambon avec sauce au maroille doré au four","friand et roulé au fromage","tomates farcie","cannelloni ","pâtes fraîche maison","crêpes au fromage","purée poisson panné","frites fricandelle","choux de Bruxelles et côtes de porc","rôti orlophe et pomme de terre ou fritte","moule (ou coque) / frite","hamburger ou kebab fait maison","saucisse lentille","cassoulet","choux rouge au lardons et pomme de terre","fondue","raclette","gauffre","soupe de légumes et beignet de pomme de terre","pancake","croissant au jambon","tournedos avec pomme de terre","cuisse de grenouille pané ","gnocchi maison","blanquette de veau avec son riz","gratin de pâtes","boeuf bourguignon","tripes avec des frites ","pot-au-feu","bouché à la reine","boudin blanc ou noir accompagnement au choix","poêlé de légumes"," gâteau de pomme de terre"]
    rand=randint(0,len(l)-1)
    return (searchRecipe(init(),0,l[rand],0,3,4)[0])

print(magicButton())