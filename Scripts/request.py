import requests


def read_webpage(url):
    try:
        # Eine GET-Anfrage an die URL senden, um den HTML-Inhalt der Webseite abzurufen
        headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS aarch64 15359.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.62 Safari/537.36'}
        response = requests.get(url, headers=headers)
        
        # Den HTML-Inhalt der Antwort extrahieren
        html_content = response.text
        
        # Den HTML-Inhalt zurückgeben
        return html_content
        
    except requests.exceptions.RequestException as e:
        # Fehlerbehandlung, falls ein Fehler bei der Anfrage auftritt
        print("Fehler beim Einlesen der Webseite:", e)
        return " "
    


USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0'
    'Mozilla/5.0 (X11; CrOS x86_64 15999.99.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5754.1 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; LIFETAB E1080X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; LaTabStandRB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; TEOX103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; S22_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla / 5.0(Windows NT 10.0; WOW64; rv: 52.0) Gecko / 20100101 Firefox / 52.0',
    'Mozilla 5.0 (Windows NT 10.0; Win32; x86; rv:88.0) Gecko/20100101 Firefox/88.0.1',
    'Mozilla 5.0 (Windows NT 10.0; Win32; x86; rv;88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (X11; Linux x86_64; Chromium GOST) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; U; Linux x86_64; rv:116.0esr) Gecko/20171214 Firefox/116.0esr',
    'Mozilla/5.0 (X11; Linux x86_64; Quest Pro) AppleWebKit/537.36 (KHTML, like Gecko) OculusBrowser/27.1.0.11.62.475067835 SamsungBrowser/4.0 Chrome/112.0.5615.179 VR Safari/537.36',
    'Mozilla/5.0 (X11; U; Linux i686; rv:123.0esr) Gecko/20112401 Firefox/123.0esr',
    'Mozilla/5.0 (X11; Linux x86_64) Gecko/20011604 Firefox/120.0',
    'Mozilla/5.0 (X11; Linux x86_64) Gecko/20070914 Firefox/118.0',
    'Mozilla/5.0 (X11; Linux i686; en-US) Gecko/20002104 Firefox/122.0esr',
    'Mozilla/5.0 (Windows NT 10.0; rv:115.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:102.0) Gecko/20100101 Goanna/6.2 Firefox/102.0 PaleMoon/32.2.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:200.0) Gecko/20100101 Firefox/200.0 f645f118e1ed5824f57251e898d8c3a2+',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; x64; rv:115.0esr) Gecko/20100101 Firefox/115.0esr',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_1; rv:116.0) Gecko/20110101 Firefox/116.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2; rv:121.0) Gecko/20000101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13; rv:115.0) Gecko/20110101 Firefox/115.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_2; rv:123.0esr) Gecko/20010101 Firefox/123.0esr',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.4788.5',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0 (Edition Yx 05),'
    'Mozilla 5.0 (Linux; U; Android 13) Chrome/104.0.5112.99',
    'Mozilla/5.0 (Android 13; Mobile; rv:101.0) Gecko/101.0 Firefox/101.0',
    'Mozilla/5.0 (Linux; Android 13; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.83 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.95 AtContent/98.5.2194.95',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.100',
    'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.1518.53',
    'Mozilla/5.0 (Linux; Android 13; RMX3521) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.1518.70',
    'Mozilla/5.0 (Linux; Android 12; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.0.0',
    'Mozilla/5.0 (Linux; Android 12; Infinix X6815B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.1518.80',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/109.0.1518.80 Version/16.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/109.0.1518.80 Version/16.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 13; SM-A226B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.1518.53',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.49',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1474.0',
    'Mozilla/5.0 (iPad; CPU Ipad OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148',
    'Mozilla/5.0 (iPad; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/12.0.0 Mobile/15A5370a Safari/602.1',
    'Mozilla/5.0 (X11; CrOS x86_64 15393.12.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS aarch64 15359.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.62 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS aarch64 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS aarch64 15269.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 15269.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 15178.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS aarch64 15178.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 15075.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS aarch64 15075.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
]