import json

games = {'matches':[]}

for i in range(1,10+1):
    # Json_games = urllib2.urlopen(url)
    f = open('data/matches' + str(i) + '.json', 'r')
    games_cur = json.load(f)
    games['matches'].append(games_cur['matches'])

games['matches'][0]['stats']['championsKilled']
