from bs4 import BeautifulSoup
import json


def extract_affiliate_links(html_content):    
    soup = BeautifulSoup(html_content, 'html.parser')

    # Finde alle <a>-Tags
    a_tags = soup.find_all('a', href=True)
    #print("A_Tags:" + str(len(a_tags)))
    
    # Liste für Affiliate-Links mit Tags
    affiliate_links_with_tags = []
    
    # Überprüfe jeden <a>-Tag
    for tag in a_tags:
        link = tag['href']
        # Check if the tag has a rel attribute with "sponsored", "nofollow" or "noopener"
        if (is_affiliate_link(link) and check_rel(tag)):
            # Speichere den Link und den gesamten <a>-Tag als String
            affiliate_links_with_tags.append({'link': link, 'tag': str(tag), 'location': get_parent_tags(tag)})

    # Gib die gefundenen Affiliate-Links zurück
    return affiliate_links_with_tags

def getTextLength(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Nur den Textinhalt extrahieren
    text_content = soup.get_text()
    # Länge des Textinhalts
    text_content_length = len(text_content)

    return text_content_length

def check_rel(tag):
    if ('rel' in tag.attrs and any(keyword in tag['rel'] for keyword in ["sponsored", "nofollow", "noopener"])):
        return True
    else:
        return False

def get_parent_tags(tag):
    parents = []
    parent = tag.find_parent()
    while parent is not None:
        parents.append(parent.name)
        parent = parent.find_parent()
    return parents
# Define the sets of keywords
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
    ]
def is_affiliate_link(link):
    
    
    # Check if the link matches any of the keyword sets
    for keyword_set in keyword_sets:
        if all(keyword in link for keyword in keyword_set):
            return True
    return False

