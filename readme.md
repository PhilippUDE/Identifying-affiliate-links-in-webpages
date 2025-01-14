EN:
Description: A python tool that extracts all affiliate links of a web document and scores this webpage according to its number and prominence of affiliate links.

Input in main.py file (line 10 & 11): 
    HTML Document(s) - name of the Documents should match the ID of the CSV File;

    CSV File:
    id,url,name of SE,position,

Output:
    Result.json File with one entry for every HTML Document in the Directory

    Structure:
    [
        {
            "Link": {
                "url": "",
                "pos": ""
            }
        },
        {
            "Affiliate Links": 
        },
        {
            "Durschnittliche Hervorhebungsstaerke":
        },
        {
            "Durschnittliche Position":
        },
        {
            "Score":
        },
        {
            "textLength":
        },
        {
            "relScore":
        }
    ]

DE:

Beschreibung: Ein Python-Tool, das alle Affiliate-Links eines Web-Dokuments extrahiert und diese Webseite nach der Anzahl und Prominenz der Affiliatelinks bewertet.

Input in der Datei main.py (Zeile 10 & 11): 
    HTML-Dokument(e) - der Name des Dokuments sollte mit der ID der CSV-Datei übereinstimmen;

    CSV-Datei:
    id,url,Name der SE,Position,

Ausgabe:
    Result.json Datei mit einem Eintrag für jedes HTML Dokument im Verzeichnis

    Aufbau:
    [
        {
            "Link": {
                "url": "",
                "pos": ""
            }
        },
        {
            "Affiliate Links": 
        },
        {
            "Durschnittliche Hervorhebungsstaerke":
        },
        {
            "Durschnittliche Position":
        },
        {
            "Score":
        },
        {
            "textLength":
        },
        {
            "relScore":
        }
    ]

