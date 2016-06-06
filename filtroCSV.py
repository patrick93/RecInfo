#coding = UTF-8
import csv

f = open('teste.csv')
csv_f = csv.reader(f)
lista_de_queries = [] 
PESQUISA_GOOGLE = " - Pesquisa Google"

for row in csv_f:
	
	if row[0] == "url":
		if PESQUISA_GOOGLE in row[3]:
				query = row[3]
				query = query.replace(PESQUISA_GOOGLE, "")
				lista_de_queries.append({'query': query, 'time': row[1]})


with open("queries.csv", "w") as output_file:
    dict_writter = csv.DictWriter(output_file, fieldnames=['query', 'time'])
    dict_writter.writerows(lista_de_queries)