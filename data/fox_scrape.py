from bs4 import BeautifulSoup as soup
import requests as req
import csv

header = ['player','games','starts','goals','assists','shots_on_goal','shots','yellow','red']

with open('epl_stats.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(header)

url_root = 'https://www.foxsports.com/soccer/stats?competition=1&season=20190&category=STANDARD&pos=0&team=0&isOpp=0&sort=3&sortOrder=0&page='

for i in range(1,11):

    page_html = req.get(url_root+str(i)).content

    page_soup = soup(page_html, 'html.parser')

    player_table = page_soup.findAll('table',{'class':'wisbb_standardTable'})[0].tbody

    player_rows = player_table.findAll('tr')

    for player_row in player_rows:

        player = player_row.a.span.text
        print('NAME: ' + player)
        player_data = player_row.findAll('td')

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