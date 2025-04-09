from static_data.prizepicks_scraped import scraped_data
from static_data.player_data import player_to_id_map
from static_data.pistons_game_logs import pistons_logs
from static_data.team_data import points_b5, points_t5
import json
import requests

raw_json = json.loads(scraped_data)
projections = raw_json['data']
all_players = raw_json['included']

#get specific projections that are over a certain minimum score
def get_player_ids_for_projections(projection_type, min_line_score):
    player_ids = []
    for projection in projections:
        attributes = projection['attributes']
        if attributes['stat_display_name'] == projection_type and attributes['line_score'] > min_line_score and attributes['odds_type'] != 'demon':
            player_ids.append(projection['relationships']['new_player']['data']['id'])
    return player_ids


#get all projections for a specfic player
def get_all_projections_for_player(player_id):
    player_projs = []
    for projection in projections:
        if projection['relationships']['new_player']['data']['id'] == player_id:
            proj_type = projection['attributes']['stat_display_name']
            line_score = projection['attributes']['line_score']
            average_id = projection['relationships']['stat_average']['data']['id']
            d = dict()
            d[proj_type] = line_score
            d["average_id"] = average_id
            player_projs.append(d)
    return player_projs

# get specific projection for a player (pass in id, type (i.e. 'Points'), and style (standard, goblin, demon))
def get_projection_for_player(player_id, projection_type, projection_style):
    player_projs = []
    for projection in projections:
        attributes = projection['attributes']
        if projection['relationships']['new_player']['data']['id'] == player_id and attributes['stat_display_name'] == projection_type and attributes['odds_type'] == projection_style:
            proj_type = projection['attributes']['stat_display_name']
            line_score = projection['attributes']['line_score']
            average_id = projection['relationships']['stat_average']['data']['id']
            d = dict()
            d[proj_type] = line_score
            d['average' + proj_type + 'ID'] = average_id
            player_projs.append(d)
    return player_projs

# pass in ids and get names
def get_player_names_for_ids(player_ids):
    player_names = []
    for id in player_ids:
        player_obj = next(item for item in all_players if item['id'] == id and item['type'] == 'new_player')
        player_names.append(player_obj['attributes']['display_name'])
    return player_names

def get_player_names_and_positions_for_ids(player_ids):
    player_position_list = []
    for id in player_ids:
        player_obj = next(item for item in all_players if item['id'] == id and item['type'] == 'new_player')
        player_position_list.append((player_obj['attributes']['display_name'], player_obj['attributes']['position']))
    return player_position_list

# pass a player name and get their team if it exists
def get_team_from_player_name(player_name):
    player_team = "team not found!"
    for player in all_players:
        if player['type'] == 'new_player' and player['attributes']['display_name'] == player_name:
            player_team = player['attributes']['team']
            break
    #print(player_team)
    return player_team

# pass a player name and get the id if it exists
def get_id_from_player_name(player_name):
    player_id = "player not found!"
    for player in all_players:
        if player['type'] == 'new_player' and player['attributes']['display_name'] == player_name:
            player_id = player['id']
            break
    return player_id

# player averages are stored in their own objects and referenced by a separate id than player id. pass in a list of average ids 
# (average_points_id, average_reb_id, etc.) and get the numerical averages back returned as a list
def get_all_averages_for_player(average_ids):
    averages = []
    for avg_id in average_ids:
        for dat in all_players:
            if dat['type'] == 'stat_average' and dat['id'] == avg_id:
                averages.append(dat['attributes']['average'])
    return averages

# pass in a player name and type of stat and this method will return his or her average over the last 5 games in that stat
# example call: get_player_last_five_average_for_stat('Stephen Curry', '3-PT Made')
# example response: Stephen Curry averages 4 3-PT Made over his last 5
def get_player_last_five_average_for_stat(player_name, stat_type):
    id = get_id_from_player_name(player_name)
    player_proj = get_projection_for_player(id, stat_type, 'goblin')
    averages = get_all_averages_for_player([player_proj[0]['average' + stat_type + 'ID']])
    print(player_name + " averages " + str(averages[0]) + " " + stat_type + " over his last 5")

# find all players whose average exceeds their projection by the passed in threshold
def get_players_outperforming_averages(projection_type, exceeding_threshold):
    player_dict = dict()
    for projection in projections:
        attributes = projection['attributes']
        average_id = 0
        if attributes['stat_display_name'] == projection_type and attributes['odds_type'] == 'standard':
            projected_line = attributes['line_score']
            average_id = projection['relationships']['stat_average']['data']['id']
        if average_id:
            averages = get_all_averages_for_player([average_id])
            #print("average: " + str(averages[0]) + ", line + threshold: " + str(projected_line + exceeding_threshold))
            if averages[0] > projected_line + exceeding_threshold:
                player_id = projection['relationships']['new_player']['data']['id']
                player_names = get_player_names_for_ids([player_id])
                print(str(player_names[0]) + " averages " + str(averages[0]) + " " + projection_type + " over his last 5 and his line is " + str(projected_line))
                player_dict[player_names[0]] = averages[0] - projected_line

    return player_dict

# find all players whose average exceeds their projection by the passed in threshold
def get_players_underperforming_averages(projection_type, exceeding_threshold):
    player_dict = dict()
    for projection in projections:
        attributes = projection['attributes']
        average_id = 0
        if attributes['stat_display_name'] == projection_type and attributes['odds_type'] == 'standard':
            projected_line = attributes['line_score']
            average_id = projection['relationships']['stat_average']['data']['id']
        if average_id:
            averages = get_all_averages_for_player([average_id])
            #print("average: " + str(averages[0]) + ", line + threshold: " + str(projected_line + exceeding_threshold))
            if projected_line - exceeding_threshold > averages[0]:
                player_id = projection['relationships']['new_player']['data']['id']
                player_names = get_player_names_for_ids([player_id])
                print(str(player_names[0]) + " averages " + str(averages[0]) + " " + projection_type + " over his last 5 and his line is " + str(projected_line))
                player_dict[player_names[0]] = averages[0] - projected_line

    return player_dict

def get_teams_against_for_projection(projection_type):
    player_dict = dict()
    for projection in projections:
         attributes = projection['attributes']
         if attributes['stat_display_name'] == projection_type and attributes['odds_type'] == 'standard':
            team_against = attributes['description']
            player_id = projection['relationships']['new_player']['data']['id']
            player_names_and_positions = get_player_names_and_positions_for_ids([player_id])
            for name, position in player_names_and_positions:
                player_dict[name] = (team_against, position)
    return player_dict

def get_list_of_positions(prize_picks_position):
    if prize_picks_position == 'G':
        return ['PG', 'SG']
    elif prize_picks_position == 'G-F' or prize_picks_position == 'F-G':
        return ['SG', 'SF']
    elif prize_picks_position == 'F':
        return ['SF', 'PF']
    elif prize_picks_position == 'F-C' or prize_picks_position == 'C-F':
        return ['PF', 'C']
    else:
        return ['C']
    
def get_player_api_id_from_name(player_name, team):
    player_id = -1
    team_map = player_to_id_map[team]
    if player_name in team_map:
        player_id = team_map[player_name]
    return player_id


#print(get_teams_against_for_projection('FG Made'))
player_matchups = get_teams_against_for_projection('Points')
players_with_good_mu = set()
players_with_bad_mu = set()
for player in player_matchups:
    matchup = player_matchups[player][0]
    pos = player_matchups[player][1]
    for position in points_b5:
        good_teams = points_b5[position]
        bad_teams = points_t5[position]
        if matchup in good_teams and position in get_list_of_positions(pos):
            players_with_good_mu.add(player)
        if matchup in bad_teams and position in get_list_of_positions(pos):
            players_with_bad_mu.add(player)
        

#print("players with good points matchups: ")
good_mu_ids = []
for player in players_with_good_mu:
    good_mu_ids.append(get_player_api_id_from_name(player, get_team_from_player_name(player)))

bad_mu_ids = []
for player in players_with_bad_mu:
    bad_mu_ids.append(get_player_api_id_from_name(player, get_team_from_player_name(player)))

first_ten_goods = good_mu_ids[0:10]
# print(first_ten_goods)
# print(len(bad_mu_ids))

url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

headers = {
	"x-rapidapi-key": "ba38032bdfmshf1fd2f352189168p1262bfjsnc553b23cf593",
	"x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
}

print(players_with_good_mu)
print(first_ten_goods)
f = open("game_logs.txt", "x")
for player_id in first_ten_goods:
    if player_id != 3414 and player_id != 2801 and player_id != 46:
        querystring = {"id":str(player_id),"season":"2024"}
        response = requests.get(url, headers=headers, params=querystring)
        f.write(str(response.json()))
f.close()


# outperformers = get_players_outperforming_averages('Points', 5)
# underperformers = get_players_underperforming_averages('Points', 5)

# for outperformer in outperformers:
#     if outperformer in players_with_good_mu:
#         print(outperformer + " plays for " + get_team_from_player_name(outperformer) + " and is a good bet for over in points")

# for underperformer in underperformers:
#     if underperformer in players_with_bad_mu:
#         print(underperformer + " plays for " + get_team_from_player_name(underperformer) + " and is a good bet for over in points")



# ids = get_player_ids_for_projections('Assists', 10)
# print(get_player_names_for_ids(ids))

# print(get_projection_for_player('188017', 'Points', 'standard'))

# zion_id = get_id_from_player_name('Zion Williamson')
# zion_projections = get_all_projections_for_player(zion_id)
# zion_average_ids = []
# for zion_proj in zion_projections:
#     zion_average_ids.append(zion_proj['average_id'])
#get_players_outperforming_averages('Assists', 1)
#print("\n")
#get_players_outperforming_averages('Fantasy Score', 5)

# url = "https://api-nba-v1.p.rapidapi.com/players"

# headers = {
# 	"x-rapidapi-key": "ba38032bdfmshf1fd2f352189168p1262bfjsnc553b23cf593",
# 	"x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
# }

# team_number = 40

# while team_number < 50:
#     querystring = {"team":str(team_number),"season":"2024"}
#     response = requests.get(url, headers=headers, params=querystring)
#     raw_json = response.json()
#     player_list = raw_json['response']
#     player_dict = dict()
#     for player in player_list:
#         player_dict[player['firstname'] + " " + player['lastname']] = player['id']
#     print(player_dict)
#     print('\n')
#     team_number += 1

# points = 0
# games_played = 0
# guards = []
# forwards = []
# centers = []
# positionless = []


# for player in pistons_logs:
#     log = pistons_logs[player]
#     position = log[0]['pos']
#     if position == 'PG' or position == 'SG' or position == 'G':
#         guards.append(player)
#     elif position == 'SF' or position == 'PF' or position == 'F':
#         forwards.append(player)
#     elif position == 'C':
#         centers.append(player)
#     else:
#         positionless.append(player)

# print("Pistons")
# print("Guards")
# print(guards)
# print("Forwards")
# print(forwards)
# print("Centers")
# print(centers)
# print("Other")
# print(positionless)
