from google_api import get_links
from find_query import get_friends_links

def friend_search(query):
	google_links = get_links(query)
	friends_link = get_friends_links(query)
	scored_links = []

	for link in google_links:
		if link in friends_link:
			scored_links.append({'url': link, 'score': 1})
		else:
			scored_links.append({'url': link, 'score': 0})

	print(sorted(scored_links, key=lambda x: x['score'], reverse=True))
	

friend_search("hindsight github")

