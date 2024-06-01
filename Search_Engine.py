'''
    File name: Search_Engine.py
    Author: SoupAndWife
    Date created: 4/20/2013
    Python Version: 3.8.3
'''

import requests
from bs4 import BeautifulSoup
from PIL import Image
import urllib
import os
import shutil
import time

element_dic = {"Fire": "zo1", "Water": "zo2", "Sand": "zo3", "Wind": "zo4", "Light": "zo5", "Dark": "zo6"}

weapon_dic = {"Ken": "bu1", "Dagger": "bu2", "Spear": "bu3", "Axe": "bu4", "Staff": "bu5", "Gun": "bu6",
          "Fist": "bu7", "Arrow": "bu8", "Music": "bu9", "Do": "bu10"}

skill_dic = {}

types_dic = {}

method_dic = {}

unleashed_dic = {}


class SearchKey:
    element = []
    weapon = []

    def __init__(self, e=[], w=[]):
        for key in e:
            self.element.append(element_dic[key])
        for key in w:
            self.weapon.append(weapon_dic[key])

    def getElement(self):
        return self.element
    
    def getWeapon(self):
        return self.weapon

class SearchEngine:
    url = "https://xn--bck3aza1a2if6kra4ee0hf.gamewith.jp/article/show/74390#"

    def __init__(self, keywords):
        element_keys = keywords.getElement()
        weapon_keys = keywords.getWeapon()

        for key in element_keys:
            self.url += (key + ",")
        for key in weapon_keys:
            self.url += (key + ",")
        # self.url = self.url[:-1]
        
        print(self.url)

    def runSearch(self):
        raw_html = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})

        print(raw_html.text) # Debug

        return raw_html
          

# Testing purpose
# def main():
#     keywords = SearchKey(["Fire", "Water"], ["Ken", "Dagger", "Music"])

#     print(keywords.element)
#     print(keywords.weapon)

#     searcher = SearchEngine(keywords)

#     searcher.runSearch()



# if __name__ == "__main__":
#     main()