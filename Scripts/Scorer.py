import json

# Liste der Container Tags und deren Punktzahl
container_tags = {'footer': 1,'main': 2, 'section': 3, 'nav': 4, 'aside': 5,  'article': 6, 'header':7}

# Funktion zur Berechnung der Punkte basierend auf den Kriterien
def calculate_points(affiliate_links, url, length, pos, searchengine):
    total_rep_points = 0  # Variable zum Speichern der Gesamtsumme der Repräsentationüunkte
    total_locations_points = 0 # Variable zum Speichern der Gesamtsumme der Positionspunkte
    # For schleife um über die gefunden Affiliate-Links zu interieren
    for link in affiliate_links:
        # Extrahiere die Werte für class, img, style und h Tags
        class_count = (len(link.get('tag', '').split('class="')) - 1)
        img_count = (link.get('tag', '').count('<img '))
        style_count = link.get('tag', '').count('style=')
        h_tag_count = sum(link.get('tag', '').count('<h{0}'.format(i)) for i in range(1, 7))
        location_points = 0 # Variabel um Positionspunktzahl für Affiliate-Link zu berechnen
        # for schleife um Position des Affiliate-Links zu bestimmen und Punktzahl zu vergeben
        for tags in container_tags:
            if tags in link.get('location'):
                location_points += container_tags[tags]

        # Punkte basierend auf der Anzahl der Tags vergeben
        rep_points = class_count*0.5 + img_count*2 + style_count + h_tag_count
        # Messwerte zu Link speciher
        link['class_count'] = class_count 
        link['img_count'] = img_count 
        link['style_count'] = style_count 
        link['h_tag_count'] = h_tag_count 
        link['rep_points'] = rep_points
        link['loc_points'] = location_points        

        # Punkte zur Gesamtsumme hinzufügen
        total_rep_points += rep_points  
        total_locations_points += location_points

    # Durchschnitt der Punkte berechnen
    average_rep_points = total_rep_points / len(affiliate_links) if affiliate_links else 0
    average_locations_points = total_locations_points / len(affiliate_links) if affiliate_links else 0

    # Score und Score in relation zu Seitenlänge berchnen
    score = len(affiliate_links) + average_rep_points + 2*average_locations_points
    relScore = (score / length) if length else 0

    # Ergebnisse zurückgeben (Tupel aus zwei Liste: 1. Messwerte, 2. Affiliate Links)
    return [{'Link': {'url': url, 'pos': pos, 'searchengine': searchengine}},{'Affiliate Links': len(affiliate_links)}, {'Durschnittliche Hervorhebungsstaerke': average_rep_points}, {'Durschnittliche Position': average_locations_points}, {'Score': score},{'textLength': length}, {'relScore': relScore*10000}], affiliate_links 

# Funktion zum Speichern der Ergebnisse in einer neuen JSON-Datei
def save_results_to_json(results, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

