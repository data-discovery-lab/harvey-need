# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:44:34 2017

SimpleDataFilter: Filters out datafile based on a list of of seed words. 
A new file will be saved based on the words in the seed lists.

Dataset Format: This programs handels .txt files that have data entryies 
seperated by line and each record seperated by SOH excel delimater.

@author: Josh Stuve
"""

import os
import json
import time


#Initializers
#For Mac
#testDataFolder = '/Users/joshuastuve/Desktop/Houston-Harvey/Test_Data/'
#rawDataFolder = '/Volumes/Untitled/HarveyResearch/Raw_Data/'
#cleanDataFolder = '/Users/joshuastuve/Desktop/Houston-Harvey/Clean_Data/'
#filterDataFolder = '/Users/joshuastuve/Desktop/Houston-Harvey/Filter_Data/Filter_Main_02/'
#rescueDataFolder = '/Users/joshuastuve/Desktop/Houston-Harvey/Rescue_Data/'

#For PC
rawData = '/home/long/DDL/project-data/harvey-need/test/'
jsonData = '/home/long/DDL/project-data/harvey-need/test-output/'

SOH='\x01' #Excel Delimted characters in data set




def hasWord(text, word):
    try:
        text.index(word)
        return True
    except:
        return False

def existOneWordFromList(text, wordList):
    for word in wordList:
        if hasWord(text, word):
            return True

    return False

def isHarveyRelated(text):
    if text == '' or len(text) < 1:
        return False

    wordList = ["harvey", "hurricane", "flood"]
    return existOneWordFromList(text, wordList)

def isNeedTweet(text):
    if text == '' or len(text) < 1:
        return False

    wordList = ["water"]
    wordList.append("diaper")
    wordList.append("bottl")
    wordList.append("perishable")
    wordList.append("suppl")
    wordList.append("formula")
    wordList.append("food")
    wordList.append("cooler")
    wordList.append("protein")
    wordList.append("wipe")
    wordList.append("blanket")
    wordList.append("deodorant")
    wordList.append("donat")
    wordList.append("deodorant")
    wordList.append("granola")
    wordList.append("cloth")
    wordList.append("underwear")
    wordList.append("beddi")
    wordList.append("necessit")
    wordList.append("toilet")
    wordList.append("volunteer")
    wordList.append("doctor")
    wordList.append("worker")
    wordList.append("physician")
    wordList.append("emergency")
    wordList.append("medic")
    wordList.append("hygiene")
    wordList.append("shampoo")
    wordList.append("conditioner")
    wordList.append("hospital")
    wordList.append("aid")
    wordList.append("batter")
    wordList.append("tooth")
    wordList.append("feminine")
    wordList.append("tampon")
    wordList.append("animal")
    wordList.append("pupp")
    wordList.append("trapped")
    wordList.append("stuck")
    wordList.append("rescue")
    wordList.append("boat")
    wordList.append("towel")
    wordList.append("help")
    wordList.append("power")
    wordList.append("gas")
    wordList.append("health")

    return existOneWordFromList(text, wordList)
#Functions
def initialDataFilter(source, dest):
    fileCount = 1
    tweetCount = 1
    for filename in os.listdir(source):
        lineCount = 1
        # jsonDataFile = open("{}{}.txt".format(dest,filename.split(".")[0]), 'w')
        jsonDataFile = open("{}{}.txt".format(dest,filename.split(".")[0]), 'w')
        with open("{}{}".format(source, filename), "r" ,encoding="utf-8-sig") as sourceDataFile:
            for line in sourceDataFile:
                jsonLine = convertToJSON(line)
                if jsonLine == False:
                    continue
                tweet = jsonLine["tweet_text"]
                # if not isHarveyRelated(tweet):
                #     continue
                # if not isNeedTweet(tweet):
                #     continue

                # json.dump(jsonLine, jsonDataFile)
                line = jsonLine["tweet_id"] + "|" + jsonLine["tweet_text"]
                jsonDataFile.write(line)
                jsonDataFile.write('\n')
                print("File: {} Line: {} Found: {}".format(fileCount, lineCount, tweetCount))
                tweetCount = tweetCount + 1
            lineCount = lineCount + 1

            jsonDataFile.flush()

        fileCount = fileCount + 1
        
def convertToJSON(rawString):
    data = {}
    splitLine = rawString.split(SOH)
    if(len(splitLine) >= 28):
        
        data['tweet_id'] = splitLine[0]
        data['tweet_text'] = splitLine[1]
        # data['point_coordinates'] = splitLine[2]
        # data['post_type'] = splitLine[3]
        # data['truncated'] = splitLine[4]
        # data['in_reply_to'] = splitLine[5]
        # data['post_time'] = splitLine[6]
        # data['NA1'] = splitLine[7] #Unknown ID
        # data['profile_url_img'] = splitLine[8]
        # data['language'] = splitLine[9]
        # data['user_id'] = splitLine[10]
        # data['background_img'] = splitLine[11]
        # data['twitter_name'] = splitLine[12]
        # data['place_id'] = splitLine[13]
        # data['place_city'] = splitLine[14]
        # data['place_city_state'] = splitLine[15]
        # data['place_country'] = splitLine[16]
        # data['location_type'] = splitLine[17]
        # data['geo_url'] = splitLine[18]
        # data['location'] = splitLine[19]
        # data['place_shape'] = splitLine[20]
        # data['place_url'] = splitLine[21]
        # data['full_name'] = splitLine[22]
        # data['city_country'] = splitLine[23]
        # data['NA4'] = splitLine[24] #Unknown Int
        # data['NA5'] = splitLine[25] #Unknown Int
        # data['NA6'] = splitLine[26] #Unknown Int
        # data['profile_created'] = splitLine[27]
        return data
    return False
#Main
if __name__ == '__main__':
    start = time.time()
    initialDataFilter(rawData, jsonData)
    end = time.time()
    print("Process Time: {} seconds".format(end - start))
