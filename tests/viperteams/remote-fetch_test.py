import viperteams
import pytest
import os

def test_fetch(httpserver):
	httpserver.serve_content(open('tests/stubs/teams.json').read())
	teams = viperteams.fetch(httpserver.url)
	assert len(teams) == 10
	assert teams[5].name == "Shine"

def test_set_all_team_properties(httpserver):
	httpserver.serve_content(open('tests/stubs/teams.json').read())
	teams = viperteams.fetch(httpserver.url)
	assert teams[0].id == "51803e2c5f23eaddb300006e"
	assert teams[0].slug == "moonglade"
	assert teams[0].name == "mOOnGLaDe"
	assert teams[0].image_url == ""
	assert teams[0].race == "Zerg"
	assert teams[0].full_name == "Andrew Pender"
	assert teams[0].country == "Australia"

def test_dictionary (httpserver):
	httpserver.serve_content(open('tests/stubs/teams.json').read())
	teams = viperteams.fetch_dictionary(httpserver.url)
	assert teams['life'].full_name == "Seung Hyun Lee" 