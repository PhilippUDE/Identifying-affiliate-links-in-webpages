import json

# Pfad zur JSON-Datei
json_file_path = 'C:\\Users\\phili\\OneDrive - Universitaet Duisburg-Essen\\Bachelorarbeit\\Algo\\JSON\\Result4.json'
txt_file_path = 'C:\\Users\\phili\\OneDrive - Universitaet Duisburg-Essen\\Bachelorarbeit\\Algo\\JSON\\avg3.txt'

# JSON-Datei einlesen
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialisiere Variablen für die Berechnungen
search_engines = ['Google_DE', 'Bing_DE']
results = {se: {
    'total_score': 0,
    'total_affiliate_links': 0,
    'total_highlight_strength': 0,
    'total_position': 0,
    'total_relScore': 0,
    'total_entries': 0,
    'pos_scores': {},
    'pos_affiliate_links': {}
} for se in search_engines}

# Durchlaufe jeden Eintrag in den Daten
for entry in data:
    if isinstance(entry, list) and len(entry) > 0:
        # Bestimme die Suchmaschine (Google oder Bing)
        searchengine = next((item.get('Link', {}).get('searchengine') for item in entry if 'Link' in item), None)
        if searchengine in results:
            # Extrahiere die relevanten Werte
            score = next((item.get('Score', 0) for item in entry if 'Score' in item), 0)
            affiliate_links = next((item.get('Affiliate Links', 0) for item in entry if 'Affiliate Links' in item), 0)
            highlight_strength = next((item.get('Durschnittliche Hervorhebungsstaerke', 0) for item in entry if 'Durschnittliche Hervorhebungsstaerke' in item), 0)
            position = next((item.get('Durschnittliche Position', 0) for item in entry if 'Durschnittliche Position' in item), 0)
            relScore = next((item.get('relScore', 0) for item in entry if 'relScore' in item), 0)
            pos = next((item.get('Link', {}).get('pos', '0') for item in entry if 'Link' in item), '0')

            # Berechnung der Durchschnittswerte pro Suchmaschine
            results[searchengine]['total_score'] += score
            results[searchengine]['total_affiliate_links'] += affiliate_links
            results[searchengine]['total_highlight_strength'] += highlight_strength
            results[searchengine]['total_position'] += position
            results[searchengine]['total_relScore'] += relScore
            results[searchengine]['total_entries'] += 1
            
            if pos not in results[searchengine]['pos_scores']:
                results[searchengine]['pos_scores'][pos] = {'score_sum': 0, 'count': 0}
                results[searchengine]['pos_affiliate_links'][pos] = {'affiliate_links_sum': 0, 'count': 0}
            
            results[searchengine]['pos_scores'][pos]['score_sum'] += score
            results[searchengine]['pos_scores'][pos]['count'] += 1
            results[searchengine]['pos_affiliate_links'][pos]['affiliate_links_sum'] += affiliate_links
            results[searchengine]['pos_affiliate_links'][pos]['count'] += 1

# Ergebnisse in einer Textdatei speichern
with open(txt_file_path, 'w', encoding='utf-8') as file:
    for se in search_engines:
        total_entries = results[se]['total_entries']
        # Durchschnittswerte berechnen
        average_score = results[se]['total_score'] / total_entries if total_entries > 0 else 0
        average_affiliate_links = results[se]['total_affiliate_links'] / total_entries if total_entries > 0 else 0
        average_highlight_strength = results[se]['total_highlight_strength'] / total_entries if total_entries > 0 else 0
        average_position = results[se]['total_position'] / total_entries if total_entries > 0 else 0
        average_relScore = results[se]['total_relScore'] / total_entries if total_entries > 0 else 0

        # Durchschnittlichen Score und Affiliate Links pro Position berechnen
        avg_pos_scores = {pos: (data['score_sum'] / data['count']) for pos, data in results[se]['pos_scores'].items()}
        avg_pos_affiliate_links = {pos: (data['affiliate_links_sum'] / data['count']) for pos, data in results[se]['pos_affiliate_links'].items()}

        # Position mit dem höchsten durchschnittlichen Score und Affiliate Links finden
        max_pos = max(avg_pos_scores, key=avg_pos_scores.get, default=None)
        max_pos_score = avg_pos_scores.get(max_pos, 0)

        max_pos_avg_affiliate_links = max(avg_pos_affiliate_links, key=avg_pos_affiliate_links.get, default=None)
        max_avg_affiliate_links = avg_pos_affiliate_links.get(max_pos_avg_affiliate_links, 0)

        # Position mit den absolut meisten Affiliate Links finden
        max_pos_total_affiliate_links = max(results[se]['pos_affiliate_links'], key=lambda pos: results[se]['pos_affiliate_links'][pos]['affiliate_links_sum'], default=None)
        max_total_affiliate_links = results[se]['pos_affiliate_links'].get(max_pos_total_affiliate_links, {}).get('affiliate_links_sum', 0)

        # Schreibe Ergebnisse für jede Suchmaschine
        file.write(f"Suchmaschine: {se}\n")
        file.write(f"Durchschnittlicher Score: {average_score:.2f}\n")
        file.write(f"Durchschnittliche Affiliate Links: {average_affiliate_links:.2f}\n")
        file.write(f"Durchschnittliche Hervorhebungsstärke: {average_highlight_strength:.2f}\n")
        file.write(f"Durchschnittliche Position: {average_position:.2f}\n")
        file.write(f"Durchschnittlicher relScore: {average_relScore:.2f}\n")
        file.write(f"Position mit dem höchsten durchschnittlichen Score: {max_pos} (Score: {max_pos_score:.2f})\n")
        file.write(f"Position mit den durchschnittlich meisten Affiliate Links: {max_pos_avg_affiliate_links} (Avg Affiliate Links: {max_avg_affiliate_links:.2f})\n")
        file.write(f"Position mit den absolut meisten Affiliate Links: {max_pos_total_affiliate_links} (Total Affiliate Links: {max_total_affiliate_links})\n")

        # Schreibe die avg_pos_scores und avg_pos_affiliate_links detailliert in die Datei
        file.write(f"\nDurchschnittliche Scores pro Position für {se}:\n")
        for pos, avg_score in avg_pos_scores.items():
            file.write(f"Position {pos}: {avg_score:.2f}\n")
        
        file.write(f"\nDurchschnittliche Affiliate Links pro Position für {se}:\n")
        for pos, avg_aff_links in avg_pos_affiliate_links.items():
            file.write(f"Position {pos}: {avg_aff_links:.2f}\n")
        
        file.write(f"\nAffiliate Links pro Position (gesamt) für {se}:\n")
        for pos, data in results[se]['pos_affiliate_links'].items():
            file.write(f"Position {pos}: {data['affiliate_links_sum']} Affiliate Links (in {data['count']} Einträgen)\n")
        
        file.write(f"\nTotal entries für {se}: {total_entries}\n\n")

print(f"Ergebnisse wurden erfolgreich in {txt_file_path} gespeichert.")
