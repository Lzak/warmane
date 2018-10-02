import requests
import time

g1 = requests.get("http://armory.warmane.com/api/guild/Ice+Crown+Citadel/Lordaeron/summary").json()
time.sleep(5)
g2 = requests.get("http://armory.warmane.com/api/guild/Icecrown+Citadel+Raiders/Lordaeron/summary").json()

f = open("roster.txt", 'w')


for member in g1['roster']:
    data = []
    data.append(member['name'])
    data.append(member['level'])
    data.append(member['gender'])
    data.append(member['race'])
    data.append(member['class'])
    data.append(member['achievementpoints'])
    if type(member['professions']) != type([]):
        for p in member['professions']['professions']:
            data.append(p['name'])
            data.append(p['skill'])
    else:
        data += ["", "", "", ""]

    data.append(g1['name'])
    data = [str(x) for x in data]

    f.write('\t'.join(data))
    f.write('\n')


for member in g2['roster']:
    data = []
    data.append(member['name'])
    data.append(member['level'])
    data.append(member['gender'])
    data.append(member['race'])
    data.append(member['class'])
    data.append(member['achievementpoints'])
    if type(member['professions']) != type([]):
        for p in member['professions']['professions']:
            data.append(p['name'])
            data.append(p['skill'])
    else:
        data += ["", "", "", ""]

    data.append(g2['name'])
    data = [str(x) for x in data]

    f.write('\t'.join(data))
    f.write('\n')

f.close()
