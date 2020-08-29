import requests
from bs4 import BeautifulSoup
import pprint

#res = requests.get("https://news.ycombinator.com/news")
#print(res)
#soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)
#print(soup.body)
#print(soup.body.contents)
#print(soup.find_all('div'))
#print(soup.find_all('a'))  -->  returns a list of <a> tags
#print(soup.title)
#print(soup.a)  -->  only first <a> tag
#print(soup.find('a'))  -->  only first <a> tag
#print(soup.find(id="up_24247561"))
#print(soup.select('#score_24247561'))
#links = soup.select('.storylink')
#votes = soup.select('.score')
#subtext = soup.select('.subtext')
#print(votes[0])
#print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k : k['votes'], reverse = True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		#print(vote)
		if len(vote):
			points = int(vote[0].getText().replace(' points',''))
			#print(points)
			if points > 99:
				hn.append({'title' : title, 'link' : href, 'votes' : points})
	return sort_stories_by_votes(hn)

def create_mega_link(num_pages):
	mega_link = []
	mega_subtext = []
	for x in range(num_pages):
		res = requests.get(f"https://news.ycombinator.com/news?p={x+1}")
		soup = BeautifulSoup(res.text, 'html.parser')
		mega_link += soup.select('.storylink')
		mega_subtext += soup.select('.subtext')
	return create_custom_hn(mega_link, mega_subtext)

num_pages = int(input("Enter the number of hacker news pages u want to see : "))
pprint.pprint(create_mega_link(num_pages))