import pygal.maps.world as maps
from populationData import getCountryCode

map = maps.World()
map.title = "Americas"

map.add("North America", ['us', 'mx', 'ca'])
map.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv']) 
map.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

map.render_to_file("americas.svg")
