import json

# Funktion zum Laden der bereits analysierten Daten aus der JSON-Datei
def load_analyzed_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

container_tags = {'nav': 1,'footer': 2, 'main': 3, 'section': 4, 'header': 5, 'aside': 6,  'article': 7}

# Funktion zur Berechnung der Punkte basierend auf den Kriterien
def calculate_points(affiliate_links, url, length, pos):
    total_rep_points = 0  # Variable zum Speichern der Gesamtsumme der Punkte
    total_locations_points = 0
    for item in affiliate_links:
        # Extrahiere die Werte für class, img, style und h Tags
        class_count = (len(item.get('tag', '').split('class="')) - 1)
        img_count = (item.get('tag', '').count('<img '))
        style_count = item.get('tag', '').count('style=')
        h_tag_count = sum(item.get('tag', '').count('<h{0}'.format(i)) for i in range(1, 7))
        location_points = 0
        for tags in container_tags:
            if tags in item.get('location'):
                location_points += container_tags[tags]

        # Punkte basierend auf der Anzahl der Tags vergeben
        rep_points = class_count*0.5 + img_count*2 + style_count + h_tag_count
        item['class_count'] = class_count 
        item['img_count'] = img_count 
        item['style_count'] = style_count 
        item['h_tag_count'] = h_tag_count 
        item['rep_points'] = rep_points
        item['loc_points'] = location_points        

        # Punkte zur Gesamtsumme hinzufügen
        total_rep_points += rep_points  
        total_locations_points += location_points

    # Durchschnitt der Punkte berechnen
    average_rep_points = total_rep_points / len(affiliate_links) if affiliate_links else 0
    average_locations_points = total_locations_points / len(affiliate_links) if affiliate_links else 0

    score = len(affiliate_links) + average_rep_points + 2*average_locations_points
    relScore = (score / length) if length else 0

    return [{'Link': {'url': url, 'pos': pos}},{'Affiliate Links': len(affiliate_links)}, {'Durschnittliche Hervorhebungsstaerke': average_rep_points}, {'Durschnittliche Position': average_locations_points}, {'Score': score},{'textLength': length}, {'relScore': relScore*10000}], affiliate_links 

# Funktion zum Speichern der Ergebnisse in einer neuen JSON-Datei
def save_results_to_json(results, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

'''
# JSON-Datei mit den analysierten Daten laden
input_json_file = 'JSON/www.chip.de.json'

analyzed_data = load_analyzed_data(input_json_file)

# Berechnung der Punkte für jeden Link
results = calculate_points(analyzed_data)

# Ergebnisse in einer neuen JSON-Datei speichern
output_json_file = f'JSON\{input_json_file}_with_points.json'
save_results_to_json(results, output_json_file)'''