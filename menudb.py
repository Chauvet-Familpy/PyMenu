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
    doc["menuList"].append({"url":detailed_recipe["url"],"name":recipe["name"],"ingredients":detailed_recipe["ingredients"],"step":detailed_recipe['steps']})
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

es=init()
print(searchRecipe(es,0,"boeuf",0,2,2))