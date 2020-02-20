from bs4 import BeautifulSoup as soup
import requests as req
import csv

header = ['player','games','starts','goals','assists','shots_on_goal','shots','yellow','red']

with open('epl_stats.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(header)

test_url = 'https://www.foxsports.com/soccer/stats?competition=1&season=20190&category=standard&sort=3'

page_html = req.get(test_url).content

page_soup = soup(page_html, 'html.parser')

player_rows = page_soup.findAll('table',{'class':'wisbb_standardTable'}).tbody

for player_row in player_rows:

    player = player_row.a.span.text

    player_data = player_row.tr.findAll('td')
    games = player_data[1].text
    starts = player_data[2].text
    goals = player_data[4].text
    assists = player_data[5].text
    shots_on_goal = player_data[6].text
    shots = player_data[7].text
    yellow = player_data[8].text
    red = player_data[9].text

    newrow = [player, games, starts, goals, assists, shots_on_goal, shots, yellow, red]

    with open('epl_stats.csv', 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(newrow)