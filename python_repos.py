from pprint import pprint

import requests

url = ('https://api.github.com/search/repositories?q=language:python&sort'
       '=stars')
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo in repo_dicts:
    print(f"\nName: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository URL: {repo['html_url']}")
    print(f"Description: {repo['description']}")

# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(f"{key}: {repo_dict[key]}")
