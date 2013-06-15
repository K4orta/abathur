import urllib2, json
from team import Team

def fetch(url, limit=1000):
	raw_teams = fetch_json(url, limit) 
	return [unpack_team(team) for team in raw_teams]

def fetch_dictionary(url, limit=1000):
	teams = fetch(url, limit)
	return {team.slug: team for team in teams}

def fetch_json(url, limit):
	res = urllib2.urlopen(url + '?per_page=' + str(limit))
	out = res.read()
	return json.loads(out)


def unpack_team(team):
	new_team = Team()
	new_team.name = team['name']
	new_team.slug = team['slug']
	new_team.id = team['id']
	new_team.country = team['country']
	new_team.race = team['race']
	new_team.full_name = team['full_name']
	new_team.country = team['country']
	new_team.image_url = team['image_url']
	return new_team


if __name__ is "__main__":
	teams = fetch("")
	print(teams.length)