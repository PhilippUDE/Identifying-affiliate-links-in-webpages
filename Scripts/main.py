import random
from LinkExtractor import extract_affiliate_links, getTextLength
from Scorer import *
from request import *
import csv
import os

urls = []
daten = []
directory_path = "C:\\Users\\phili\\Desktop\\rat_affiliate_results\\html"
csv_path = 'C:\\Users\\phili\\Desktop\\rat_affiliate_results\\rat_affiliate_links.csv'

def get_score(item):
    for d in item:
        if 'Score' in d:
            return d['Score']
    return 0

# Funktion, um die URL zu einer gegebenen ID zu finden
def get_url_and_position_for_id(csv_path, target_id):
    with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] == target_id:
                return row['url'], row['position']
    return None, None


html_files = [file for file in os.listdir(directory_path) if file.endswith('.html')]
num_html_files = len(html_files)
x=0



for html_file in html_files:
    file_path = os.path.join(directory_path, html_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Extrahiere die ID aus dem Dateinamen
    target_id = os.path.splitext(html_file)[0]  # Annahme: ID ist der Dateiname ohne .html
    url, position = get_url_and_position_for_id(csv_path, target_id)
    if not url:
        print(f"Keine URL für ID {target_id} gefunden.")
        continue

    affiliate_links = extract_affiliate_links(html_content)
    print(f"Progress: {x}/{num_html_files} ({(x/num_html_files)*100:.2f}%)")
    results = calculate_points(affiliate_links, url, getTextLength(html_content), position)  
    daten.append(results[0])
    x += 1



# Sortieren der Liste nach Score-Wert
sorted_data = sorted(daten, key=get_score, reverse=True)

save_results_to_json(sorted_data, f"JSON/Result2.json")

