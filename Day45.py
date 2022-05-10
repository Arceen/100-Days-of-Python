from distutils.file_util import move_file
from bs4 import BeautifulSoup
import requests
# with open('Day45_website.html', encoding='utf-8') as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, features='lxml')

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.get('href'))
    
# heading = soup.find(name='h1', id='name')
# print(heading.getText())

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# url = 'https://news.ycombinator.com/show'
# res = requests.get(url)
# # print(res.text)
# soup = BeautifulSoup(res.text, 'lxml')
# links = soup.find_all(class_='titlelink')
# scores = soup.find_all(class_='score')
# # print(len(links))
# # print(len(scores))
# index = -1
# curr_score = 0
# for i in range(len(links)):
#     score = int(scores[i].getText()[:-7])
#     if curr_score < score:
#         curr_score = score
#         index = i
    
# print(links[index].getText()[9:])
# print(links[index].get('href'))
# print(scores[index].getText()[:-7])

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
res = requests.get(url)
print(res.text.count('h3'))
soup = BeautifulSoup(res.text, 'lxml')
print(soup.find_all('h3', {'class':'title'}))
movie_list = [i.text for i in soup.find_all('h3',{'class':'title'})][::-1]
print(movie_list)
with open('Day45_top_100_movies.txt', 'w') as f:
    for i in movie_list:
        f.write(i+'\n')
    
    

# print(soup.prettify())
# titles = soup.find_all(['h1', 'h2', 'h3'])
# print(titles)
# print(titles)
# for title in titles:
#     print(title.text)