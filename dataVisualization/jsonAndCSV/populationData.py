import json
from pygal.maps.world import COUNTRIES, World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

def getCountryCode(countryName):
    for code, country in COUNTRIES.items():
        if country == countryName:
            return code
    return None

with open("population_data.json") as file:
    contents = json.load(file)

populations1, populations2, populations3 = {}, {}, {}
for dict in contents:
    if dict['Year'] == '2010':
        code = getCountryCode(dict['Country Name'])
        if code:
            population = int(float(dict['Value']))
            if population < 10000000:
                populations1[code] = population
            elif population < 100000000:
                populations2[code] = population
            else:
                populations3[code] = population

mapStyle = RS("#0088ff", base_style=LCS)
map = World(style=mapStyle)
map.title = "2010 Populations"

map.add("0-10m", populations1)
map.add("10-100m", populations2)
map.add("100m+", populations3)

map.render_to_file("populationMap.svg")
    