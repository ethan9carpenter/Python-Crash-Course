import requests, pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
request = requests.get(url)
print("Status code:", request.status_code)

response = request.json()
print("Total Repositories:", response['total_count'])

repoResponse = response['items']
print("Number of Repositrories Returned:", len(repoResponse))

'''print()
keys = {'Owner': 'owner', 
        'Name': 'name',
        'Stars': 'stargazers_count',
        "Repository": 'created_at',
        'Updated': 'updated_at',
        'Description': 'description'}

for repo in repoResponse:
    for name, key in keys.items():
        if key == 'owner':
            print(name+":", repo[key]['login'])
        else:
            print(name+":", repo[key])
    print()'''
    
names, chartDict = [], []

for repo in repoResponse:
    names.append(repo['name'])
    dict = {
        'value': repo['stargazers_count'],
        'label': repo['description'],
        'xlink': repo["html_url"]
        }
    if not dict['label']:
        dict['label'] = '' 
    chartDict.append(dict)
    
style = LS("#333366", base_style=LCS)
config = pygal.Config()
config.x_label_rotation = 45
config.show_legend = False
config.title_font_size = 24
config.label_font_size = 14
config.major_label_font_size = 18
config.truncate_label = 15
config.width = 1000
config.style = style
config.show_y_guides = False

chart = pygal.Bar(config=config)
chart.title = "Most Starred Python Repositories on Github"
chart.x_labels = names
    
chart.add('', chartDict)

chart.render_to_file("mostStarredPythonRepos.svg")




















