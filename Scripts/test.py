import requests


def resolve_url(link):
    try:
        response = requests.head(link, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        print(f"Fehler beim Auflösen des Links {link}: {e}")
        return link

print(resolve_url("http://haushaltsgeraetetest.de/information/produkt/B0CJ9BC1ZG/haushaltsgeraetetest-sub16-21"))