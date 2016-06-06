import requests

API_KEY = "AIzaSyAhrht1pkJNuAw3sQuUFh34v-Yoaa9adhI"
CX = "010532648492414585372:wgsvyzd_u2e"

def get_links(query):
	links = []
	url = "https://www.googleapis.com/customsearch/v1"
	params = {'key': API_KEY, 'cx': CX, 'q': query}
	response = requests.get(url, params=params)
	content = response.json()
	for item in content['items']:
		links.append(item['link'])
	return links
