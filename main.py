import requests


def superhero_intelligence(name, token='2619421814940190'):
    url = f'https://superheroapi.com/api/{token}/search/{name}'
    response = requests.get(url)
    response_json = response.json()
    intelligence = response_json['results'][0]['powerstats']['intelligence']
    return (int(intelligence), name)

super_superheroes = []
superheroes = ['Hulk', 'Captain America', 'Thanos']
superheroes_intelligence = [superhero_intelligence(name) for name in superheroes]
max_intelligence = max(superheroes_intelligence)[0]
for intll, hero in superheroes_intelligence:
    if intll == max_intelligence:
        super_superheroes.append(hero)

print(*super_superheroes, sep='\n')