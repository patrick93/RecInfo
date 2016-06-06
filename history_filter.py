#coding = UTF-8
import csv

f = open('teste.csv')
csv_f = csv.reader(f)
lista_url = []

for row in csv_f:
	if row[0] == "url":
		lista_url.append({'time': row[1], 'url': row[2]})


with open("history.csv", "w") as output_file:
    dict_writter = csv.DictWriter(output_file, fieldnames=['time', 'url'])
    dict_writter.writerows(lista_url)