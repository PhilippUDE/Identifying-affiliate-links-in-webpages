from LinkExtractor import extract_affiliate_links, getTextLength
from Scorer import *
import csv
import os


results = [] # Liste um die Ergebnisse der einzelnen Webseiten zu speichern
directory_path = "" # Pfad zu den HTML Dokumenten
csv_path = '' # Pfad zur CSV Datei mit Informationen zu den HTML Dokumenten 

# Funktion um den Score einer Webseite auszulesen
def get_score(item):
    for d in item:
        if 'Score' in d:
            return d['Score']
    return 0

# Funktion, um die URL, die Suchergebnisposition und Suchmaschine zu einer gegebenen ID eines HTML-Dokumentes zu finden
def get_url_and_position_for_id(csv_path, target_id):
    with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] == target_id:
                return row['url'], row['position'], row['name']
    return None, None, None


# Liste der HTML Dateien im Verzeichnis
html_files = [file for file in os.listdir(directory_path) if file.endswith('.html')]
# Anzahl der HTML Datein
num_html_files = len(html_files)
# Progress Counter
x=0


# for Schleife um über alle HTML-Datein zu iterieren
for html_file in html_files:
    # Pfad zur HTML Datei zusammensetzen
    file_path = os.path.join(directory_path, html_file)
    # HTML Datei einlesen
    with open(file_path, 'r', encoding='utf-8') as file: 
        html_content = file.read()
    # Extrahiere die ID aus dem Dateinamen
    target_id = os.path.splitext(html_file)[0]  # Annahme: ID ist der Dateiname ohne .html
    # URL, Suchergebnissposition und Suchmaschine zur gegeben ID auslesen
    url, position, searchengine = get_url_and_position_for_id(csv_path, target_id)
    # Affiliate Link eines HTML-Dokuments extrahieren
    affiliate_links = extract_affiliate_links(html_content)
    # Fortschritt ausgeben (optional)
    print(f"Progress: {x}/{num_html_files} ({(x/num_html_files)*100:.2f}%)")
    # Score berechnen
    score = calculate_points(affiliate_links, url, getTextLength(html_content), position, searchengine)
    # Ergebnisse ohne Liste der Affiliate Links speichern  
    results.append(score[0])
    # Progress erhöhen
    x += 1

# Sortieren der Liste nach Score-Wert
sorted_data = sorted(results, key=get_score, reverse=True)
# Ergebnisse in JSON Datei speichern
save_results_to_json(sorted_data, f"JSON/Result.json")

