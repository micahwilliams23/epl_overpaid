from bs4 import BeautifulSoup as soup
import requests as req
import csv

test_url = 'https://www.foxsports.com/soccer/stats?competition=1&season=20190&category=standard&sort=3'

page_html = req.get(test_url).content

page_soup = soup(page_html, 'html.parser')

player_row = page_soup.findAll('table',{'class':'wisbb_standardTable'})[0].tbody

player = player_row.a.span.text

games = player_row.tr.td

print(games)