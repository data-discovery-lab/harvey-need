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
rawData = 'G:/HarveyResearch/OG_Rescue_Data/Raw_Data/'
jsonData = 'G:/HarveyResearch/OG_Rescue_Data/JSON_Data/'

SOH='\x01' #Excel Delimted characters in data set

#Functions
def initialDataFilter(source, dest):
    fileCount = 1
    tweetCount = 1
    for filename in os.listdir(source):
        lineCount = 1
        jsonDataFile = open("{}{}.txt".format(dest,filename.split(".")[0]), 'w')
        with open("{}{}".format(source, filename), "r" ,encoding="utf-8-sig") as sourceDataFile:
            for line in sourceDataFile:
                jsonLine = convertToJSON(line)
                json.dump(jsonLine, jsonDataFile)
                jsonDataFile.write('\n')
                print("File: {} Line: {} Found: {}".format(fileCount, lineCount, tweetCount))
                tweetCount = tweetCount + 1
            lineCount = lineCount + 1
        fileCount = fileCount + 1
        
def convertToJSON(rawString):
    data = {}
    splitLine = rawString.split(SOH)
    if(len(splitLine) >= 28):
        
        data['tweet_id'] = splitLine[0]
        data['tweet_text'] = splitLine[1]
        data['point_coordinates'] = splitLine[2]
        data['post_type'] = splitLine[3]
        data['truncated'] = splitLine[4]
        data['in_reply_to'] = splitLine[5]
        data['post_time'] = splitLine[6]
        data['NA1'] = splitLine[7] #Unknown ID
        data['profile_url_img'] = splitLine[8]
        data['language'] = splitLine[9]
        data['user_id'] = splitLine[10]
        data['background_img'] = splitLine[11]
        data['twitter_name'] = splitLine[12]
        data['place_id'] = splitLine[13]
        data['place_city'] = splitLine[14]
        data['place_city_state'] = splitLine[15]
        data['place_country'] = splitLine[16]
        data['location_type'] = splitLine[17]
        data['geo_url'] = splitLine[18] 
        data['location'] = splitLine[19]
        data['place_shape'] = splitLine[20]
        data['place_url'] = splitLine[21]
        data['full_name'] = splitLine[22]
        data['city_country'] = splitLine[23]
        data['NA4'] = splitLine[24] #Unknown Int
        data['NA5'] = splitLine[25] #Unknown Int
        data['NA6'] = splitLine[26] #Unknown Int
        data['profile_created'] = splitLine[27]
    return data
#Main
if __name__ == '__main__':
    start = time.time()
    initialDataFilter(rawData, jsonData)
    end = time.time()
    print("Process Time: {} seconds".format(end - start))
