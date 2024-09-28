from bs4 import BeautifulSoup

html_content = """
<html>
  <body>
    <a href="https://example.com">Link 1</a>
    <a href="https://example2.com">Link 2</a>
    <a href="https://example3.com">Link 3</a>
  </body>
</html>
"""

# BeautifulSoup initialisieren
soup = BeautifulSoup(html_content, 'html.parser')

# Alle <a> Tags finden
links = soup.find_all('a')

# Typ überprüfen
print(links)  # <class 'bs4.element.ResultSet'>

# Iteriere durch das ResultSet und gebe die Links aus
for link in links:
    print(link.get('href'))
