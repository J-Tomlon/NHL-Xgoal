import pandas as pd  
import numpy as np   
import requests
from nhldata import moneypuck

def get_moneypuck_shots():
    
    # This is the correct connector class
    mp = moneypuck.Connector()

    # Get shot data for specific seasons
    shots = mp.shots_season(season=2022)
    
    # Example: print first shot
    print(shots[0])

'''
def get_nhl_shots():
    
    client = NHLClient()

    # Replace with a valid game ID (e.g., 2023020456)
    game_id = "2023020456"
    pbp = client.game_center.game_play_by_play(game_id=game_id)

    # Filter for shot events
    shots = [play for play in pbp['plays'] if play['event'] == 'SHOT']

    # Print shot details
    for shot in shots:
        print(f"{shot['player']} took a shot from {shot['coordinates']} for {shot['team']}")
'''



def get_shots_from_game(game_id):
    url = f"https://statsapi.web.nhl.com/api/v1/game/{game_id}/feed/live"
    response = requests.get(url)
    data = response.json()

    plays = data['liveData']['plays']['allPlays']
    shots = [play for play in plays if play['result']['eventTypeId'] == 'SHOT']

    for shot in shots:
        player = shot['players'][0]['player']['fullName']
        team = shot['team']['name']
        coords = shot.get('coordinates', {})
        print(f"{player} ({team}) shot from {coords}")

# Example game ID
get_shots_from_game("2017010001")

