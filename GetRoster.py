import requests
import time
import sys



class Warmane(object):
    def __init__(self):
        self.URL_BASE = "http://armory.warmane.com/api/"
        self.URL_GUILD = "guild/"
        self.OUTPUT_FILE = "roster.txt"

    def getGuildURL(guild_name, realm):
        return URL_BASE + URL_GUILD + guild_name.strip().replace(' ', '+') + '/' + realm.strip() + '/'
        




# ------------------------------- Config ---------------------------------------



#guild_links =   [getGuildURL("Ice Crown Citadel", "Lordaeron"),
#                getGuildURL("Icecrown Citadel Raiders", "Lordaeron")]

guild_links = [getGuildURL("Global Chat Degens", "Lordaeron")]



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


if __name__ == "__main__":
