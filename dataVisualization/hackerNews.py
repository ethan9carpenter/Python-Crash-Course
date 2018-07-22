import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/item/9884165.json'
request = requests.get(url)

print('Status Code:', request.status_code)

submmissionIDs = request.json()
submissionDicts = {}

for submission in submmissionIDs:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission) + '.json'
    subRequest = requests.get(url)

    print(subRequest.status_code)
    
    response = subRequest.json()
    print(response)
    dict = {
        'title': response['title'],
        'url': 'https://news.ycombinator.com/item?id=' + str(submission),
        'numComments': response.get('descendants', 0)#checks dict for key, and returns 0 if key not found
        }
    submissionDicts.append(dict)

submissionDicts = sorted(submissionDicts, key=itemgetter('numComments'), reverse=True)
for article in submissionDicts:
    print("Title:", article['title'])
    print('URL:', article['url'])
    print('Total Number of Comments:', article['numComments'], '\n')
    
    
    
    
    
    
    
