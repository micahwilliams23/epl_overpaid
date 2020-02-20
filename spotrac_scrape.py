from bs4 import BeautifulSoup as soup
import requests as req
import csv

def clean_money(dirty_money):

    return(dirty_money.replace('£','').replace(',',''))

test_url = 'https://www.spotrac.com/epl/afc-bournemouth/contracts/'\

page_html = req.get(test_url).content

page_soup = soup(page_html, 'html.parser')

rows = page_soup.findAll('tr')[1:]

for player_row in rows:
        
    player = player_row.findAll('td')[0].a.text
    position = player_row.findAll('td')[1].text
    age = player_row.findAll('td')[2].text
    contract_value_dirty = player_row.findAll('td')[3].span[0].text
    contract_length = player_row.findAll('td')[3].span[1].text
    transfer_fee_dirty = player_row.findAll('td')[5].span[0].text

    print(player, age)

    exit(1)