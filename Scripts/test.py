import csv
import json
from collections import defaultdict

# Pfade zu den Dateien
json_path = 'C:\\Users\\phili\\OneDrive - Universitaet Duisburg-Essen\\Bachelorarbeit\\Algo\\JSON\\Result4.json'
csv_path = 'C:\\Users\\phili\\Desktop\\rat_affiliate_results\\rat_affiliate_links.csv'
output_json_path = 'C:\\Users\\phili\\OneDrive - Universitaet Duisburg-Essen\\Bachelorarbeit\\Algo\\JSON\\ResultQuery2.json'

# Funktion, um die Query für eine URL in der CSV-Datei zu finden
def get_query_for_url(csv_path, url):
    with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['url'] == url:
                return row['query']
    return None

# JSON-Datei laden
with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Dictionaries, um zu zählen, wie oft eine Query mindestens einen Affiliate-Link hat, getrennt nach Suchmaschine
query_count_google = defaultdict(int)
query_count_bing = defaultdict(int)
x = 0
# Über die JSON-Daten iterieren und URLs sowie Affiliate-Links überprüfen
for entry in data:
    # Suche den Dictionary-Eintrag mit dem Schlüssel 'Link'
    link_entry = next((item for item in entry if 'Link' in item), None)

    if link_entry and 'url' in link_entry['Link']:
        print(x)
        x = x+1
        url = link_entry['Link']['url']
        search_engine = link_entry['Link'].get('searchengine', '').lower()

        # Suche nach der Query für die URL in der CSV-Datei
        query = get_query_for_url(csv_path, url)

        if query:
            # Überprüfen, ob es Affiliate-Links gibt
            affiliate_links = next((item['Affiliate Links'] for item in entry if 'Affiliate Links' in item), 0)

            # Falls Affiliate-Links vorhanden sind, zähle die Query
            if affiliate_links > 0:
                if 'google' in search_engine:
                    query_count_google[query] += 1
                elif 'bing' in search_engine:
                    query_count_bing[query] += 1

# Zähle, wie viele Queries mindestens eine Seite mit einem Affiliate-Link haben, getrennt nach Suchmaschine
queries_with_affiliate_links_google = len(query_count_google)
queries_with_affiliate_links_bing = len(query_count_bing)

# Ergebnis anzeigen
print(f"Anzahl der Suchanfragen mit mindestens einem Affiliate-Link (Google): {queries_with_affiliate_links_google}")
print(f"Anzahl der Suchanfragen mit mindestens einem Affiliate-Link (Bing): {queries_with_affiliate_links_bing}")

# Optional: Speichern der detaillierten Ergebnisse in einer JSON-Datei
output_data = {
    "Google": query_count_google,
    "Bing": query_count_bing
}

with open(output_json_path, 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, indent=4)

print("Ergebnisse wurden erfolgreich gespeichert.")
