import csv
import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import datetime
import logging
from datetime import timedelta
import numpy as np

from datetime import timedelta

import os.path

x_data_final = []
y_data_final = []

def scrapeWebsite(url, nameHtml):
    fileScrape = open(nameHtml,"w")

    ##request html and write into file

    f = urllib2.urlopen(url)

    fileScrape.write(f.read())
    fileScrape.close()
    f.close()

    ##use BeautifulSoup api to convert to usable format

    soup = BeautifulSoup(open(nameHtml), 'lxml')

## incase you want to look at what you're doing in file format 

##    fileHTML = open("brightonHTML.html","w")
##    fileHTML.write(str(soup))
##    fileHTML.close()

    ##find the tables from the website. [2] is the third one down 

    tableSchoolResults = soup('table', attrs={'class':'table'})[2]

    ##find fields using find_all('tr') and find_all('td')

    rowsResults = tableSchoolResults.find_all('tr')
    x_data=[]
    y_data=[]
    y_data_raw=[]
    for row in rowsResults:
        cols = row.find_all('td')
        if cols != []:
            levelString = str(cols[0])
            valuesString = str(cols[1])
            print(levelString[4:-5]+": " + valuesString[19:-6]+"%")
            x_data.append(int(valuesString[19:-6]))

    tableAverageEarnings = soup('table', attrs={'class':'table'})[8]

    rowsResults = tableAverageEarnings.find_all('tr')

    for row in rowsResults:
        cols = row.find_all('td')
        if cols != []:
            levelString = str(cols[0])
            valuesString = str(cols[1])
            print(levelString[4:-5]+": " + valuesString[21:-6]+"k")
            y_data_raw.append(valuesString[21:-6])
            break

    ##map the various data to a label for the childrens results
    for val in y_data_raw:
        if (int(val) < 22):
            y_data.append(1)
        elif (int(val) < 28):
            y_data.append(2)
        elif (int(val) < 34):
            y_data.append(3)
        elif (int(val) < 40):
            y_data.append(4)
        elif (int(val) < 46):
            y_data.append(5)
        elif (int(val) < 52):
            y_data.append(6)
        else:
            print("average is higher than 52k")
            
    print(x_data)
    print(y_data)

    ##add to final data set
    x_data_final.append(x_data)
    y_data_final.append(y_data)


    ##y_data cats <15k = 0 15k-20k = 1 20k-25k = 2 25k-35k=3 35k-45k=4 45k-60k = 5 60k+ = 6


if __name__ == "__main__":
    ##Brighton
    scrapeWebsite('https://www.findahood.com/locations/regency/6278777', "brightonData.html")
    ##London
    scrapeWebsite('https://www.findahood.com/locations/leeming/6280978', "londonData.html")
    ##Durham
    scrapeWebsite('https://www.findahood.com/locations/nevillescross/6279563', "durhamData.html")
    ##Newcastle
    scrapeWebsite('https://www.findahood.com/locations/westgate/6277033', "newcastleData.html")
    ##Bath
    scrapeWebsite('https://www.findahood.com/locations/abbey/6278260', "bathData.html")
    ##Birmingham
    scrapeWebsite('https://www.findahood.com/locations/stpauls/6277357', "birminghamData.html")
    ##Nottingham
    scrapeWebsite('https://www.findahood.com/locations/keyworthnorth/6281132', "nottinghamData.html")
    ##Market Rasen
    scrapeWebsite('https://www.findahood.com/locations/marketrasen/6280718', "marketRasenData.html")
    print(x_data_final)
    print(y_data_final)
