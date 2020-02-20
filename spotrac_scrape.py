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
        
    # scrape player's name
    player = player_row.findAll('td')[0].a.text

    # scrape player's position
    position = player_row.findAll('td')[1].text

    # scrape player's age
    age = player_row.findAll('td')[2].text

    # scrape total contract value, then clean away '£' and ','
    contract_value_dirty = player_row.findAll('td')[3].span[0].text
    contract_value = clean_money(contract_value_dirty)

    # scrape contract length
    contract_length = player_row.findAll('td')[3].span[1].text

    # scrape transfer fee, then clean away '£' and ','
    transfer_fee_dirty = player_row.findAll('td')[5].span[0].text
    transfer_fee = clean_money(transfer_fee_dirty)

    print(player, age)

    exit(1)