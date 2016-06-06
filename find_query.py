from datetime import datetime, timedelta
import csv

def match_query(query):
	file_query = open("queries.csv")
	reader_file_query = csv.DictReader(file_query, fieldnames=['query', 'time'])
	matched_queries = []

	for row in reader_file_query:
		if row['query'] == query:
			matched_queries.append(row)

	return matched_queries


def find_links(queries):
	history_file = open("history.csv")
	reader_history_file = csv.DictReader(history_file, fieldnames=['time', 'url'])
	links = []

	for query in queries:
		query_time = datetime.strptime(query['time'], '%Y-%m-%d %H:%M:%S.%f')
		plus_time = query_time+timedelta(seconds=5)
		for row in reader_history_file:
			link_time = datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S.%f')
			if query_time < link_time <= plus_time: 
				links.append(row)
	return links

def get_friends_links(query):
	queries = match_query(query)
	return [link['url'] for link in find_links(queries)]