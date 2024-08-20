import os
from bs4 import BeautifulSoup
import json

id=437735

# Pfad zur lokalen HTML-Datei
html_file_path = f"C:\\Users\\phili\\Desktop\\rat_affiliate_results\\html\\{id}.html"
text_file_path = f"JSON/Files2/{id}.txt"

# Öffnen und Lesen des Inhalts der HTML-Datei
with open(html_file_path, 'r', encoding='utf-8') as file:
    web_content = file.read()

# Erstellen eines BeautifulSoup-Objekts
soup = BeautifulSoup(web_content, 'html.parser')

# Finden aller <a> Tags, die Links enthalten
links = soup.find_all('a')

links_list = [link.get('href') for link in links if link.get('href')] #and 'http' in link.get('href')]
print(id)
print("Gesamt Links: " + str(len(links_list)))
# Pfad zur JSON-Datei
json_file_path = f"JSON\\Files2\\{id}_with_points.json"  # Ersetze 'yourfile.json' mit dem tatsächlichen Dateinamen


# JSON-Datei lesen
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Links aus der zweiten Liste extrahieren
links2 = []
for entry in data:
    for item in entry:
        if 'link' in item:
            links2.append(item['link'])
print("Affilaite Links: " + str(len(links2)))
# Links, die in links_list aber nicht in links2 sind
unique_links = [link for link in links_list if link not in links2]

print("unique Links: " + str(len(unique_links)))

# Speichern der einzigartigen Links in einer Textdatei
with open(text_file_path, 'w', encoding='utf-8') as file:
    for link in unique_links:
        file.write(link + '\n')
    file.write("\n\n\n\n----------------------------------------------------\n\n\n\n")
    for link in links2:
        file.write(link + '\n')

'''with open(f"JSON/{id}_all.txt", 'w', encoding='utf-8') as file:
    for link in links_list:
        file.write(link + '\n')'''

print(f"Links wurden erfolgreich in {text_file_path} gespeichert.")
os.system(f'code {text_file_path}')