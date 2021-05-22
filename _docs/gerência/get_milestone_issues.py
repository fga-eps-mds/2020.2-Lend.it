"""
Script to fetch GitHub API milestone issues data and parse it to MD Table

Author: Rogério Júnior
Version: 1.0
"""
import requests

from collections import defaultdict
from pprint import PrettyPrinter

query_params = {
    'milestone': input("Milestone NUMBER? "),
    'state': 'all',
    'direction': 'asc'
}

response = requests.get(
    'https://api.github.com/repos/fga-eps-mds/2020.2-Lend.it/issues', params=query_params)

print('')

if response.status_code == 200:

    zenhub_payload = {
        'X-Authentication-Token': 'e59a46decb8f31a42d20cab279bfd709556ae32728d6714588603d2b83179e0ac82f52604b847ba6'
    }
    user_name = {
        'rogerioo': 'Rogério Júnior',
        'EsioFreitas': 'Esio Gustavo',
        'youssef-md': 'Youssef Muhamad',
        'lucasdutraf': 'Lucas Dutra',
        'mateusmaiamaia': 'Mateus Maia',
        'Matheusafonsouza': 'Matheus Afonso',
        'matheusyanmonteiro': 'Matheus Monteiro',
        'Thais-ra': 'Thais Rebouças',
        'thiagompc': 'Thiago Mesquita',
        'viniciussaturnino': 'Vinícius Saturnino'
    }

    data = response.json()
    md_table = ''
    users_points = defaultdict(int)

    for issue in data:
        if not 'pull_request' in issue.keys():
            zenhub = requests.get(
                f"https://api.zenhub.com/p1/repositories/335968110/issues/{issue['number']}", headers=zenhub_payload)

            if zenhub.status_code == 200:
                zenhub = zenhub.json()
                users = ''

                for idx, user in enumerate(issue['assignees']):
                    users += f"[{user_name[user['login']]}]({user['html_url']})"

                    users_points[user_name[user['login']]
                                 ] += zenhub['estimate']['value'] / len(issue['assignees'])

                    if idx == len(issue['assignees']) - 2:
                        users += ' e '
                    elif len(issue['assignees']) > 1 and idx != len(issue['assignees']) - 1:
                        users += ', '

                try:
                    md_table += f"| [#{issue['number']}](https://github.com/fga-eps-mds/2020.2-Lend.it/issues/{issue['number']}) | {issue['title']} | {zenhub['estimate']['value'] } | {users} |\n"
                    print(f"Issue {issue['number']} Added!")
                except:
                    print(
                        f"Issue {issue['number']} missing estimate! It'll be ignored")
                    continue

    print('\n\n@@@@@@@@@@@@@@@@@@@@@@@@@ RESULT TABLE @@@@@@@@@@@@@@@@@@@@@@@@@\n' + md_table)

    print('\n\n@@@@@@@@@@@@@@@@@@@@@@@ POINTS PER USER @@@@@@@@@@@@@@@@@@@@@@@\n')
    PrettyPrinter(indent=2).pprint(dict(users_points))
