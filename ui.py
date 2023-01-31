import PySimpleGUI as sg
import stats_backend as nba

# colour scheme
sg.theme('Reddit')

# layout for menu/home page
home_layout = [
          [sg.Image('./assets/logo2.png')],
          [sg.Push(), sg.Text('Click on one of the buttons below!', font='Verdana'), sg.Push()],
          [sg.Button('Today\'s Games', font='Verdana', pad=10)],
          [sg.Button('Player Stats Search', font='Verdana', pad=10)],
          [sg.Button('Team Search', font='Verdana', pad=10, button_color="skyblue")],
          [sg.Button('Standings', font='Verdana', pad=10, button_color="skyblue")],
          [sg.Button('Help?', font='Verdana', pad=10, button_color='gray'), sg.Push(), sg.VPush(), sg.Button('Exit', font='Verdana', pad=10, button_color='red')]
         ]
# layout for player search page
player_search_layout = [
    [sg.Image('./assets/logo2.png')],
    [sg.Push(), sg.Text('Search for a player to see their stats!', font='Verdana', pad=10), sg.Push()],
    [sg.Input(key="-PLAYER-")],
    [sg.Button('Search Player', font='Verdana', pad=10)],
    [sg.Button('Help?', font='Verdana', pad=10, button_color='gray'), sg.Push(),
     sg.Button('Back to Menu', font='Verdana', pad=10), sg.Push(), sg.VPush(),
     sg.Button('Exit', font='Verdana', pad=10, button_color='red')]
]

# layout for stats display page
player_stats_layout = [
    [sg.Image('./assets/logo2.png')],
    [sg.Push(), sg.Text('Player Stats for:', font='Verdana'), sg.Push()],
    [sg.Push(), sg.Text("", font='Verdana 24 bold', key='-PLAYERNAME-'), sg.Push()],
    [sg.Text('', font='Verdana', key='-YR-', pad=5, visible=False), sg.Text('', font='Verdana', key='-TEAM-', pad=5, visible=False), sg.Text('', font='Verdana', key='-MIN-', pad=5, visible=False)],
    [sg.Text('', font='Verdana', key='-PPG-', pad=5), sg.Text('', font='Verdana', key='-REB-', pad=5), sg.Text('', font='Verdana', key='-AST-', pad=5)],
    [sg.Text('', font='Verdana', key='-STL-', pad=5), sg.Text('', font='Verdana', key='-BLK-', pad=5), sg.Text('', font='Verdana', key='-TOV-', pad=5)],
    [sg.Text('', font='Verdana', key='-FG%-', pad=5, visible=False), sg.Text('', font='Verdana', key='-3P%-', pad=5, visible=False), sg.Text('', font='Verdana', key='-FT%-', pad=5, visible=False)],
    [sg.Button('Switch to Advanced View', font='Verdana', pad=10, visible=True),
    sg.Button('Switch to Simple View', font='Verdana', pad=10, visible=False)],
    [sg.VPush()],
    [sg.Button('Help?', font='Verdana', pad=10, button_color='gray'), sg.Push(),
     sg.Button('Back to Player Search', font='Verdana', pad=10), sg.Push(), sg.VPush(),
     sg.Button('Exit', font='Verdana', pad=10, button_color='red')]
    ]

# layout for help page
help_layout = [
    [sg.Image('./assets/logo2.png')],
    [sg.Push(), sg.Text('Help Page', font='Verdana 13 bold'), sg.Push()],
    [sg.Push(), sg.Text('This page explains all the features of this app.', font='Verdana'), sg.Push()],
    [sg.Text("Today's Games:",  font='Verdana 12 bold')],
    [sg.Text("View all games being played in the NBA today.",font='Verdana')],
    [sg.Text("Player Stats Search:", font='Verdana 12 bold')],
    [sg.Text("Enter the player name you want to see stats for.", font='Verdana')],
    [sg.Text("Stat Legend", font='Verdana 12 bold')],
    [sg.Text("Stats are all displayed as PER GAME", font='Verdana')],
    [sg.Text("FG%: Field Goal Percentage", font='Verdana')], [sg.Text("3P%: Three Point Percentage", font='Verdana')],
     [sg.Text("FT%: Free Throw Percentage", font='Verdana')],
    [sg.Button('Help?', font='Verdana', pad=10, button_color='gray'), sg.Push(),
     sg.Button('Back', font='Verdana', pad=10), sg.Push(), sg.VPush(),
     sg.Button('Exit', font='Verdana', pad=10, button_color='red')]
]

# function to get today's games and create layout
def get_scoreboard_layout():
    games = nba.get_games()
    layout = [
          [sg.Image('./assets/logo2.png')],
          [sg.Push(), sg.Text("Here are today's games!", font='Verdana'), sg.Push()],
          [sg.Button('Help?', font='Verdana', pad=10, button_color='gray'), sg.Push(), sg.Button('Back to Menu', font='Verdana', pad=10),sg.Push(), sg.VPush(),
          sg.Button('Exit', font='Verdana', pad=10, button_color='red')]
         ]
    insert_index = 2
    for game in games:
        layout.insert(insert_index, [sg.Text(game, font='Verdana', relief="sunken", pad = ((0,0),(5,5)), background_color="seashell2")])
        insert_index += 1
    return sg.Column(layout, visible=False, key='-COL2-', element_justification='c')

# function to get stats of player and return tuple of data
def get_stats(player):
    stats = nba.get_player_stats(player)
    pts = (round(stats["PTS"].values[0] / stats["GP"].values[0], 1))
    reb = (round(stats["REB"].values[0] / stats["GP"].values[0], 1))
    ast = (round(stats["AST"].values[0] / stats["GP"].values[0], 1))
    stl = (round(stats["STL"].values[0] / stats["GP"].values[0], 1))
    blk = (round(stats["BLK"].values[0] / stats["GP"].values[0], 1))
    tov = (round(stats["TOV"].values[0] / stats["GP"].values[0], 1))
    min = (round(stats["MIN"].values[0] / stats["GP"].values[0], 1))
    team = stats["TEAM_ABBREVIATION"].values[0]
    year = stats["SEASON_ID"].values[0]
    fg = round(stats["FG_PCT"].values[0] * 100,1)
    thrpt = round(stats["FG3_PCT"].values[0] * 100, 1)
    ft = round(stats["FT_PCT"].values[0] *100, 1)
    return pts, reb, ast, stl, blk, tov, min, team, year, fg, thrpt, ft

# add all pages to one layout array
layouts = [[sg.Column(home_layout, key='-COL1-', element_justification='c'), get_scoreboard_layout(),
            sg.Column(player_search_layout, visible=False, key='-COL3-', element_justification='c'),
            sg.Column(player_stats_layout, visible=False, key='-COL4-', element_justification='c'),
            sg.Column(help_layout, visible=False, key='-COL5-', element_justification='c')]]

# generate window
window = sg.Window('NBA Stats', layouts, element_justification='c', size=(475, 500))

# start at layout 1 (main menu) by default
layout = 1
previous = None
player_cache = {} # not yet used, but will cache player data so doesn't need to be reloaded every search

# Event Loop
while True:
    event, values = window.read()
    print(event, values)

    # exit
    if event == sg.WIN_CLOSED or 'Exit' in event:
        break

    # change to today's game page
    if event == "Today's Games":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)

    # change to player search page
    if event == "Player Stats Search":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)

    # go back to menu page
    if "Back to Menu" in event:
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)

    # if a player is searched for, retrieve data and fill stats page out and display
    if event == "Search Player":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window["-PLAYERNAME-"].update(values["-PLAYER-"].upper())
        ppg, reb, ast, stl, blk, tov, mins, team, year, fg, thrpt, ft , = get_stats(values["-PLAYER-"])
        window["-PLAYER-"].update("")
        window["-PPG-"].update(f'Points: {ppg}')
        window["-REB-"].update(f'Rebounds: {reb}')
        window["-AST-"].update(f'Assists: {ast}')
        window["-STL-"].update(f'Steals: {stl}')
        window["-BLK-"].update(f'Blocks: {blk}')
        window["-TOV-"].update(f'Turnovers: {tov}')
        window["-MIN-"].update(f'Minutes: {mins}')
        window["-YR-"].update(f'Season: {year}')
        window["-TEAM-"].update(f'Team: {team}')
        window["-FG%-"].update(f'FG%: {fg}%')
        window["-3P%-"].update(f'3P%: {thrpt}%')
        window["-FT%-"].update(f'FT%: {ft}%')
        window[f'-COL{layout}-'].update(visible=True)

    # if a user wants to switch back to the simple view or return to search, hide advanced stats
    if event == "Switch to Simple View" or event == "Back to Player Search":
        window["-MIN-"].update(visible=False)
        window["-YR-"].update(visible=False)
        window["-TEAM-"].update(visible=False)
        window["-FG%-"].update(visible=False)
        window["-3P%-"].update(visible=False)
        window["-FT%-"].update(visible=False)
        window["Switch to Advanced View"].update(visible=True)
        window["Switch to Simple View"].update(visible=False)

    # returns to the search page
    if event == "Back to Player Search":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)

    # if a user wants to view more stats, display them
    if event == "Switch to Advanced View":
        window["-MIN-"].update(visible=True)
        window["-YR-"].update(visible=True)
        window["-TEAM-"].update(visible=True)
        window["-FG%-"].update(visible=True)
        window["-3P%-"].update(visible=True)
        window["-FT%-"].update(visible=True)
        window["Switch to Advanced View"].update(visible=False)
        window["Switch to Simple View"].update(visible=True)

    # displays the help page
    if "Help?" in event:
        window[f'-COL{layout}-'].update(visible=False)
        previous = layout
        layout = 5
        window[f'-COL{layout}-'].update(visible=True)

    # help page back button, return to previous page
    if event == "Back":
        window[f'-COL{layout}-'].update(visible=False)
        layout = previous
        window[f'-COL{layout}-'].update(visible=True)

# close on break
window.close()