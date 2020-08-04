# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib.parse
import urllib.request

import re


class Recipes(object):

	@staticmethod
	def get(url):

		html_content = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html_content, 'html.parser')

		#image_url = str(soup.find("picture", {"class": "recipe-cover-blur"}).find("img").text)
		image_url=soup.find("picture", {"class": "recipe-cover-blur"}).find('img')["src"]

		people_data=int(soup.find("span", {"class": "ingredient-variator-label"}).text.split(" ")[0])
  
		ingredients_map={}
		ingredients_data = soup.findAll("span", { "class": "recipe-ingredients-item-label"})
		for i in ingredients_data:
			try:
				quantity_data = int(i.text.split(" ")[0].replace('\n', " ").replace(",", "."))/people_data
				ingredients_map.update({i.text.replace(i.text.split(" ")[0], ""): quantity_data})
			except IOError:
				quantity_data = float(i.text.split(" ")[0].replace("\n", "").replace(",", "."))/people_data
				ingredients_map.update({i.text.replace(i.text.split(" ")[0], ""): quantity_data})
			except:
				ingredients_map.update({i.text: ""})

		rate = (soup.find("span", {"class": "rating-grade"}).text).replace("\n        ", "")

		preparation_data = soup.findAll("div", {"class": "recipe-steps-text"})

		list_instructions = []
		for i in preparation_data:
			list_instructions.append(i.text)

		try:
			name=soup.find("span", {"class":"recipe-title"}).text
		except:
			name="Inconnu"
   
		data = {
			"url": url,
			"image": image_url,
			"name": name,
			"ingredients": ingredients_map,
			"steps": list_instructions,
			"rate": rate
		}

		return data








