'''Functions related to anime pictures and stuff'''
from dotenv import load_dotenv
import random
import os
import file_load as fl

#keep track of recently searched images, max 20 images
searchedPicCache = []
#Non-Nitro maximum file size for Discord
MAX_FILE_SIZE = 8388119

def check_cache(updatedLink):
    '''Function that checks if randomly pulled image has been recently searched'''
    if updatedLink in searchedPicCache:
        return False
    elif updatedLink not in searchedPicCache and len(searchedPicCache) == 20:
        searchedPicCache.append(updatedLink)
        del searchedPicCache[0]
        return True
    else:
        searchedPicCache.append(updatedLink)
        return True

def check_file_size(updatedLink):
    '''Function that checks if randomly chosen image is within the 8MB Limit of Discord'''
    fileSize = os.path.getsize(updatedLink)
    if fileSize >= MAX_FILE_SIZE:
        return False
    else:
        return True

def tamamo_search():
    '''Function that searches for a random Tamamo no Mae picture saved locally'''
    folderLink = os.getenv("TAMAMO_PATH")
    updatedLink = ""
    picSearched = False

    #Keep pulling new images until unique one has been found
    while not picSearched:
        currPic = random.choice(os.listdir(folderLink))
        updatedLink = folderLink + "/" + str(currPic)
        validSize = check_file_size(updatedLink)
        if validSize:
            picSearched = check_cache(updatedLink)

    return updatedLink

def kemono_search():
    '''Function that searches a random foxgirl picture saved locally;
    Tamamo no Mae inclusive'''

    linkList = fl.file_load_kitsunesearch()
    folderLink = random.choice(linkList)
    updatedLink = ""
    picSearched = False

    while not picSearched:
        currPic = random.choice(os.listdir(folderLink))
        updatedLink = folderLink + "/" + str(currPic)
        validSize = check_file_size(updatedLink)
        if validSize:
            picSearched = check_cache(updatedLink)

    return updatedLink

def musashi_plush():
    '''Returns an imgur link to a picture of a Musashi plush'''
    picLink = 'https://imgur.com/mPDCYEK'
    return picLink
