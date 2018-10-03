import requests
import time

# ------------------------------- Config ---------------------------------------
guild_links =   ['http://armory.warmane.com/api/guild/Ice+Crown+Citadel/Lordaeron/summary',
                'http://armory.warmane.com/api/guild/Icecrown+Citadel+Raiders/Lordaeron/summary']
output_file = "roster.txt"
# ------------------------------------------------------------------------------

guilds = []
for link in guild_links:
    guilds.append(requests.get(link).json())

    # Warmane's API doesn't like to get spammed with reqs
    time.sleep(5)

f = open(output_file, 'w')

for guild in guilds:
    for member in guild['roster']:
        data = []
        data.append(member['name'])
        data.append(member['level'])
        data.append(member['gender'])
        data.append(member['race'])
        data.append(member['class'])
        data.append(member['achievementpoints'])

        # If there's 1 or 2 professions available
        if type(member['professions']) != type([]):
            for p in member['professions']['professions']:
                data.append(p['name'])
                data.append(p['skill'])
            if len(member['professions']['professions']) == 1:
                data += ["", ""]
        # Otherwise no professions available
        else:
            data += ["", "", "", ""]

        data.append(guild['name'])
        data = [str(x) for x in data]

        f.write('\t'.join(data))
        f.write('\n')

f.close()
