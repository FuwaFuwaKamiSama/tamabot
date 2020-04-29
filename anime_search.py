'''Functions related to anime pictures and stuff'''
from dotenv import load_dotenv
import random
import os
import file_load as fl

#keep track of recently searched images, max 20 images
searchedPicCache = []

def tamamo_search():
    '''Function that searches for a random Tamamo no Mae picture saved locally'''
    folderLink = os.getenv("TAMAMO_PATH")
    updatedLink = ""

    while True:
        currPic = random.choice(os.listdir(folderLink))
        updatedLink = folderLink + "/" + str(currPic)

        #Checking if random image has been recently searched
        if (updatedLink in searchedPicCache):
            continue
        elif updatedLink not in searchedPicCache and len(searchedPicCache) == 20:
            searchedPicCache.append(updatedLink)
            del searchedPicCache[0]
            break
        else:
            searchedPicCache.append(updatedLink)
            break

    return updatedLink

def foxgirl_search():
    '''Function that searches a random foxgirl picture saved locally;
    Tamamo no Mae inclusive'''

    linkList = fl.file_load_kitsunesearch()
    folderLink = random.choice(linkList)
    updatedLink = ""

    while True:
        currPic = random.choice(os.listdir(folderLink))
        updatedLink = folderLink + "/" + str(currPic)

        #Checking if random image has been recently searched
        if (updatedLink in searchedPicCache):
            continue
        elif updatedLink not in searchedPicCache and len(searchedPicCache) == 20:
            searchedPicCache.append(updatedLink)
            del searchedPicCache[0]
            break
        else:
            searchedPicCache.append(updatedLink)
            break

    return updatedLink

def musashi_plush():
    '''Returns an imgur link to a picture of a Musashi plush'''
    picLink = 'https://imgur.com/mPDCYEK'
    return picLink
