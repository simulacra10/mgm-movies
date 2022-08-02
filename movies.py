import requests
import json
from bs4 import BeautifulSoup as bs
from csv import writer

"""
Simple script to scrape the top 100 classic horror movies made by MGM Universal on IMBD,
save to CSV and JSON. 

Modules: BeautifulSoup, requests, csv, json

Author: Norman Bauer

"""
print("Requesting page...")
URL = 'https://imdb.com/list/ls000493268/'

# request the page and run it through BeautifulSoup's HTML parser.
req = requests.get(URL)
soup = bs(req.text, 'html.parser')
#find all the html elements that match my criteria and make list of them.
horror_movies = soup.find_all('h3',attrs = {"class":'lister-item-header'})

#open a csv file 'c" and start writing to it.
print("Creating CSV file ...")
with open('horror-movies.csv', 'w', encoding='utf8') as c:
    csv = writer(c)
    csv_header_row = ['Rank', 'Title','Year']
    csv.writerow(csv_header_row)
    #loop through the list, pulling out the text that I want, based on the attibutes in the html element.
    #Append a variable for the text I want and append it to a list call "list".
    for movie in horror_movies:
        rank = movie.find('span', class_="lister-item-index").text
        title = movie.find('a').text
        year = movie.find('span', class_="lister-item-year").text
        list = [rank,title,year]
        csv.writerow(list)
c.close()

#Creating the json file
print("Creating JSON file...")
with open('horror-movies.json', 'w') as j:
    #loop through the list, pulling out the text that I want, based on the attibutes in the html element.
    #Append a variable for the text I want and append it to a list call "list".
    for movie in horror_movies:
        rank = movie.find('span', class_="lister-item-index").text
        title = movie.find('a').text
        year = movie.find('span', class_="lister-item-year").text
        list = [rank,title,year]
        json.dump(list,j)
j.close()
print("Done.")
#That's all folks!

