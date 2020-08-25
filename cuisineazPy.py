from bs4 import BeautifulSoup

import urllib.parse
import urllib.request
import ast
import re
import json

class CuisineAZ(object):
    @staticmethod
    def get(uri):
        base_url = "https://www.cuisineaz.com/recettes"
        url = base_url + uri

        html_content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html_content, 'html.parser')

        #image_url = str(soup.find("picture", {"class": "recipe-cover-blur"}).find("img").text)
        image_url=soup.find("div", {"class": "content-scroll"}).find("section", {"class": "recipe_img"}).find("img")["data-src"]

        list_ingredient=[]
        ingredients_data = soup.findAll("ul", {"class": "txt-dark-gray"})
        for i in ingredients_data:
            list_ingredient.append(i.text)
        list_ingredients=list_ingredient[0].split("\n")

        list_step=[]
        step_data=soup.find("section", {"class": "borderSection instructions"}).findAll("ul", {"data-onscroll": ""})[1].findAll("p")
        for i in step_data:
            list_step.append(i.text)        
        
        rate=5

        name=soup.find("h1", {"class":"recipe-title"}).text

        data = {
            "url": url,
            "image": image_url,
            "name": name,
            "ingredients": list_ingredients,
            "step": list_step,
            "rate": rate
        }

        return data