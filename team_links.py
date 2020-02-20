from bs4 import BeautifulSoup as soup
import requests as req

list_url = 'https://www.spotrac.com/epl/'

page_html = req.get(list_url).content

page_soup = soup(page_html, 'html.parser')

team_rows = page_soup.findAll('div',{'class':'teamname'}).a

team_links = team_rows

print(team_links)

exit(1)

# with ('team_links.txt', 'w') as f:
#     f.write(+'\n')