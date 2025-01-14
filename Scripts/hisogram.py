import json
from collections import defaultdict

# Lade die JSON-Datei
file_path = 'C:\\Users\\phili\\OneDrive - Universitaet Duisburg-Essen\\Bachelorarbeit\\Algo\\JSON\\ResultQuery2.json'
with open(file_path, 'r', encoding='utf-8') as file:
    suchanfragen = json.load(file)

# Dictionary zur Zählung der Scores für Google und Bing
score_counts_google = defaultdict(int)
score_counts_bing = defaultdict(int)

# Iteriere über die Suchanfragen für Google und zähle die Scores
for query, score in suchanfragen.get('Google', {}).items():
    score_counts_google[score] += 1

# Iteriere über die Suchanfragen für Bing und zähle die Scores
for query, score in suchanfragen.get('Bing', {}).items():
    score_counts_bing[score] += 1

# Ausgabe der Häufigkeiten für Google
print("Google Suchanfragen - Score Häufigkeiten:")
for score, count in score_counts_google.items():
    print(f'Score: {score}, Häufigkeit: {count}')

# Ausgabe der Häufigkeiten für Bing
print("\nBing Suchanfragen - Score Häufigkeiten:")
for score, count in score_counts_bing.items():
    print(f'Score: {score}, Häufigkeit: {count}')
