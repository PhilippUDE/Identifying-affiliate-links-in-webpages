from bs4 import BeautifulSoup
from functools import lru_cache
import requests


# Funktion um HEAD-Anfrage zu senden
@lru_cache(maxsize=8589934592)
def resolve_url(link):
    try:
        response = requests.head(link, allow_redirects=True, timeout=1) # Timeout verkürzen falls Anfrage zu lange dauert
        return response.url
    except:
        #print(f"Fehler beim Auflösen des Links {link}: {e}")
        return link

# Funktion um Affiliate Links zu extrahieren
def extract_affiliate_links(html_content):
    # HTML Dokument parsen
    soup = BeautifulSoup(html_content, 'html.parser')
    # Finde alle <a>-Tags mit href-Attribut
    a_tags = soup.find_all('a', href=True)    
    # Liste für Affiliate-Links mit Tags
    affiliate_links_with_tags = []
    # Überprüfe jeden <a>-Tag (for Schleife)
    for tag in a_tags:
        # URL aus href-Attribut extrahieren
        link = tag['href']
        # Link auf Affiliate Link und rel Attribut untersuchen
        isAfLink = is_affiliate_link(link)
        hasRel = check_rel(tag)
        if(hasRel):
            if (isAfLink):
                # Speichere den Link und den gesamten <a>-Tag als String in der Liste
                affiliate_links_with_tags.append({'link': link, 'tag': str(tag), 'location': get_parent_tags(tag)})
            else:
                resolved_link = resolve_url(link)  # Link vor der Überprüfung auflösen
                if (is_affiliate_link(resolved_link)):
                    # Speichere den Link und den gesamten <a>-Tag als String in der Liste
                    affiliate_links_with_tags.append({'link': resolved_link, 'tag': str(tag), 'location': get_parent_tags(tag)})

    # Gib die gefundenen Affiliate-Links zurück
    return affiliate_links_with_tags

# Funktion um Länge des HTML-Dokumentes zu bestimmen
def getTextLength(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Nur den Textinhalt extrahieren
    text_content = soup.get_text()
    # Länge des Textinhalts
    text_content_length = len(text_content)
    return text_content_length

#Check if the tag has a rel attribute with "sponsored", "nofollow" or "noopener"
def check_rel(tag):
    if ('rel' in tag.attrs and any(keyword in tag['rel'] for keyword in ["sponsored", "nofollow", "noopener"])):
        return True
    else:
        return False

# Funktion um alle Parent Tags des Affiliate Links zu indetifizieren (Positionsbestimmung)
def get_parent_tags(tag):
    parents = []
    parent = tag.find_parent()
    while parent is not None:
        parents.append(parent.name)
        parent = parent.find_parent()
    return parents





'''
    Title: ecir24-seo-spam-in-search-engines source code
    Author: Janek Bevendorff, Webis
    Date: 2021
    Availability: https://github.com/webis-de/ecir24-seo-spam-in-search-engines/blob/main/warc_analysis/warc_analysis/process.py
'''
# Bekannte Affiliate-Link Sturukturen (zum Teil zitiert)
keyword_sets = [
        ["https://", "amazon", "tag=",],
        ["https://", "amazon", "tag%3D",],
        ["https://", "tag="],
        ["https://", "awin1"],
        ["https://", "ebay", "mkcid"],
        ["https://", "aliexpress", "click", "e"],
        ["https://", "bestcheck", "track"],
        ["https://", "shareasale","r.cfm"],
        ["https://", "shrsl"],
        ["https://", "clickbank", "hop"],
        ["https://", "jdoqocy","click"],
        ["https://", "anrdoezrs", "links"],
        ["https://", "flexlinks","track","a.ashx"],
        ["https://", "flexlinkspro","a.ashx"],
        ["https://", "rfsn"],
        ["https://", "pjtra", "t"],
        ["https://", "linksynergy", "t"],
        ["https://", "webgains","track","click"],    
        ["https://", "billiger","de","mc="],
        ["https://", "billiger","de","mc%3D"], 
        ["https://", "td","oo34","net","aaid="],
        ["https://", "td","oo34","net","aaid%3D"],
        ["https://", "ipn","idealo","ts"],
        ["https://", "partner","cyberport","trck","eclick"],
        ["https://", "pvn","mediamarkt","trck","eclick"],
        ["https://", "notebooksbilliger","nbbct=",],
        ["https://", "notebooksbilliger","nbbct%3D",],
        ["https://", "pvn","saturn","trck","eclick"],
    ]

# Funktion um Affiliate-Link zu identifizieren
def is_affiliate_link(link): 
    # Check if the link matches any of the keyword sets
    for keyword_set in keyword_sets:
        if all(keyword in link for keyword in keyword_set):
            return True
    return False

