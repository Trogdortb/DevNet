from urllib.request import urlopen

url = "http://www.dndbeyond.com/spells/class/artificer"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)