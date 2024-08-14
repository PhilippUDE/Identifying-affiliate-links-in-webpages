import json

# Pfad zur JSON-Datei
json_file_path = "JSON\\Files2\\448816_with_points.json"  # Ersetze 'yourfile.json' mit dem tatsächlichen Dateinamen
text_file_path = "JSON/AffiliateLink_448816.txt"  # Ersetze 'outputfile.txt' mit dem gewünschten Ausgabedateinamen

# JSON-Datei lesen
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Links aus der zweiten Liste extrahieren
links = []
for entry in data:
    for item in entry:
        if 'link' in item:
            links.append(item['link'])

# Links in einer Textdatei speichern
with open(text_file_path, 'w', encoding='utf-8') as file:
    for link in links:
        file.write(link + '\n')

print(f"Links wurden erfolgreich in {text_file_path} gespeichert.")