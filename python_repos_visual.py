import requests

from plotly.graph_objs import Bar
from plotly import offline

url = ('https://api.github.com/search/repositories?q=language:python&sort'
       '=stars')
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []

for repo in repo_dicts:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Repository',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
    'yaxis': {'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              }
}

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='github-stars.html')
