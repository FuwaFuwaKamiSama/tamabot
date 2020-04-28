'''Functions related to anime pictures and stuff'''
from dotenv import load_dotenv
import random
import os

def tamamo_search():
    '''Function that searches for a random Tamamo no Mae picture saved locally'''
    folderLink = os.getenv("TAMAMO_PATH")
    currPic = random.choice(os.listdir(folderLink))
    updatedLink = folderLink + "/" + str(currPic)
    return updatedLink

def musashi_plush():
    '''Returns an imgur link to a picture of a Musashi plush'''
    picLink = 'https://imgur.com/mPDCYEK'
    return picLink
