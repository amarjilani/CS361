# Author: Amar Jilani
# GitHub username: amarjilani
# Date: 2023-01-30
# Description: Module to allow for getting a NBA player's stats or today's games
import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static import players

# ensures all columns are displayed when printed
pd.set_option('display.max_columns', None)

def get_player_stats(playername):
    """
    Returns a datatable of the given player's stats for this season
    :param playername: full name of player
    :return: returns data frames of stats
    """
    player_id = players.find_players_by_full_name(playername)[0]["id"]
    career_stats = playercareerstats.PlayerCareerStats(player_id)
    data = career_stats.get_data_frames()
    stats = data[0]
    return stats.loc[stats['SEASON_ID'] == "2022-23"]

# formatting for scoreboard
f = "{awayTeam} {awayScore} vs. {homeTeam} {homeScore}"
def get_games():
    """
    Returns all of the current day's NBA games and their current scores
    :return:
    """
    board = scoreboard.ScoreBoard()
    games = board.games.get_dict()
    parsed_games = []
    for game in games:
        parsed_games.append((f.format(awayTeam=game['awayTeam']['teamTricode'], awayScore=game['awayTeam']['score'],
                       homeTeam=game['homeTeam']['teamTricode'], homeScore=game['homeTeam']['score'])))
    return parsed_games
