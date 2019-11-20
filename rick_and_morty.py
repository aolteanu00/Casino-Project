from flask import Flask, render_template
from data import database_builder, database_query
import urllib, json

def rickandmortyapi():
    count = 493; # this is the total number of characters in rick and morty
    page = 1
    while count > 0:
        url = urllib.request.urlopen("https://rickandmortyapi.com/api/character/?page=" + str(page))
        response = url.read()
        data = json.loads(response)
        # Use a for loop to add every element to the database
        for i in data['results']:
            database_query.rickandmortydb(i['id'], i['name'], i['image'])
            count -= 1
        page += 1
    return 0;