import json

# Pfad zur JSON-Datei
json_file_path = 'C:\\Users\\phili\\OneDrive - Universitaet Duisburg-Essen\\Bachelorarbeit\\Algo\\JSON\\Result.json'
txt_file_path = 'C:\\Users\\phili\\OneDrive - Universitaet Duisburg-Essen\\Bachelorarbeit\\Algo\\JSON\\avg.txt'

# JSON-Datei einlesen
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialisiere Variablen für die Berechnungen
total_score = 0
total_affiliate_links = 0
total_highlight_strength = 0
total_position = 0
total_relScore = 0
total_entries = 0
pos_scores = {}

# Durchlaufe jeden Eintrag in den Daten
for entry in data:
    # Überprüfen, ob der Eintrag eine Liste von Dictionaries ist
    if isinstance(entry, list) and len(entry) > 0:
        # Extrahiere die relevanten Werte
        score = next((item.get('Score', 0) for item in entry if 'Score' in item), 0)
        affiliate_links = next((item.get('Affiliate Links', 0) for item in entry if 'Affiliate Links' in item), 0)
        highlight_strength = next((item.get('Durschnittliche Hervorhebungsstaerke', 0) for item in entry if 'Durschnittliche Hervorhebungsstaerke' in item), 0)
        position = next((item.get('Durschnittliche Position', 0) for item in entry if 'Durschnittliche Position' in item), 0)
        relScore = next((item.get('relScore', 0) for item in entry if 'relScore' in item), 0)
        pos = next((item.get('Link', {}).get('pos', '0') for item in entry if 'Link' in item), '0')

        # Berechnung der Durchschnittswerte
        total_score += score
        total_affiliate_links += affiliate_links
        total_highlight_strength += highlight_strength
        total_position += position
        total_relScore += relScore
        total_entries += 1
        
        if pos not in pos_scores:
            pos_scores[pos] = {'score_sum': 0, 'count': 0}
        
        pos_scores[pos]['score_sum'] += score
        pos_scores[pos]['count'] += 1

# Durchschnittswerte berechnen
average_score = total_score / total_entries if total_entries > 0 else 0
average_affiliate_links = total_affiliate_links / total_entries if total_entries > 0 else 0
average_highlight_strength = total_highlight_strength / total_entries if total_entries > 0 else 0
average_position = total_position / total_entries if total_entries > 0 else 0
average_relScore = total_relScore / total_entries if total_entries > 0 else 0

# Durchschnittlichen Score pro Position berechnen
avg_pos_scores = {pos: (data['score_sum'] / data['count']) for pos, data in pos_scores.items()}

# Position mit dem höchsten durchschnittlichen Score finden
max_pos = max(avg_pos_scores, key=avg_pos_scores.get, default=None)
max_pos_score = avg_pos_scores.get(max_pos, 0)

# Ausgabe der Ergebnisse
print(f"Durchschnittlicher Score: {average_score:.2f}")
print(f"Durchschnittliche Affiliate Links: {average_affiliate_links:.2f}")
print(f"Durchschnittliche Hervorhebungsstärke: {average_highlight_strength:.2f}")
print(f"Durchschnittliche Position: {average_position:.2f}")
print(f"Durchschnittlicher relScore: {average_relScore:.2f}")
print(f"Position mit dem höchsten durchschnittlichen Score: {max_pos} (Score: {max_pos_score:.2f})")

with open(txt_file_path, 'w', encoding='utf-8') as file:
    file.write(f"Durchschnittlicher Score: {average_score:.2f}\n")
    file.write(f"Durchschnittliche Affiliate Links: {average_affiliate_links:.2f}\n")
    file.write(f"Durchschnittliche Hervorhebungsstärke: {average_highlight_strength:.2f}\n")
    file.write(f"Durchschnittliche Position: {average_position:.2f}\n")
    file.write(f"Durchschnittlicher relScore: {average_relScore:.2f}\n")
    file.write(f"Position mit dem höchsten durchschnittlichen Score: {max_pos} (Score: {max_pos_score:.2f})\n")

print(f"Ergebnisse wurden erfolgreich in {txt_file_path} gespeichert.")