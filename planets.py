import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name =planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

import requests

def new_fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    planet_dict = {}
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            planet_dict[name] = {
                'mass': mass,
                'orbit_period': orbit_period
            }
    return planet_dict

def find_heaviest_planet(planet_dict):
    return max(planet_dict.items(), key=lambda x: x[1]['mass'])

planets = new_fetch_planet_data()
heaviest_planet_name, heaviest_planet_attributes = find_heaviest_planet(planets)
print(f"The heaviest planet is {heaviest_planet_name} with a mass of {heaviest_planet_attributes['mass']} kg.")
