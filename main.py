import os

__author__ = 'tal89'
from bs4 import BeautifulSoup
import urllib.request
import re

linkvar = input("please provide the product link :)" + "\n")

def GrabImages(url):
    wfile = open('imglinks.txt', 'w')
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib.request.urlopen(req)
    counter = 0
    soup = BeautifulSoup(con,"html.parser")
    try:
        imgs = soup.find(class_="p-property-item")
    except:
        print('something went wrong, trying another option')



    for img in imgs.findAll(class_="item-sku-image")[1:100]:

        counter = counter + 1
        col = img.findAll('img')[0].get('bigpic')
        print(col);
        wfile.write("\n" + str(col))
    return GrabName(url);

def GrabThumbImages(url):
    wfile = open('imglinks.txt', 'a')
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib.request.urlopen(req)
    counter = 0
    soup = BeautifulSoup(con,"html.parser")
    imgs = soup.find(id="j-image-thumb-list")
    for img in imgs.findAll(class_='img-thumb-item')[1:100]:

        counter = counter + 1
        col = img.findAll('img')[0].get('src')
        col=col[:-10]
        print(col);
        wfile.write("\n" + str(col))



def GrabName(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
        con = urllib.request.urlopen(req)
        counter = 0
        soup = BeautifulSoup(con,"html.parser")
        title = soup.find(id="product-prop-2")
        title2=title.findAll(class_="propery-des")[0].get('title')
        print (title2);

        producttype=soup.find(class_="property-item")
        producttypesub=producttype.findAll(class_="propery-des")[0].get('title')
        print (producttypesub);
        nameofnewdir=producttypesub + " by " + title2;
        return nameofnewdir
    except:
        print("error getting name")
        return "error"

namefordir=GrabImages(linkvar);
GrabThumbImages(linkvar);


directory=namefordir
if not os.path.exists(directory):
    os.makedirs(directory)


def ImageDownloader():
    file = open('imglinks.txt', 'r')
    counter=0
    for line in file:
        counter+=1;
        countertext=str(counter);
        newimgfilename=directory+"/"+"img"+countertext+".jpg"
        print(newimgfilename)
        try:
            urllib.request.urlretrieve(line, newimgfilename)
            print(counter)

        except ValueError:
            print ("Oops something went wrong :(")


ImageDownloader()



input()