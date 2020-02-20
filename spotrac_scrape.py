from bs4 import BeautifulSoup as soup
import requests as req
import csv

with open('epl_data.csv') as f:
    writer = csv.writer(f)
    writer.writerow('player','position','age','contract_value','contract_length','transfer_fee')

def clean_money(dirty_money):

    return(dirty_money.replace('£','').replace(',',''))

test_url = 'https://www.spotrac.com/epl/afc-bournemouth/contracts/'\

page_html = req.get(test_url).content

page_soup = soup(page_html, 'html.parser')

rows = page_soup.findAll('tr')[1:]

for player_row in rows:

    row_td = player_row.findAll('td')
        
    # scrape player's name
    player = row_td[0].a.text

    # scrape player's position
    position = row_td[1].text

    # scrape player's age
    age = row_td[2].text

    # scrape total contract value
    contract_value = row_td[3].span.text

    # scrape contract length
    contract_length = row_td[3].findAll('span')[1].text

    # scrape transfer fee, then clean away '£' and ','
    transfer_fee_dirty = row_td[5].span.text

    transfer_fee = clean_money(transfer_fee_dirty)

    with open('epl_data.csv') as f:
        writer = csv.writer(f)
        writer.writerow(player, position, age, contract_value, contract_length, transfer_fee)