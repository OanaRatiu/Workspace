import re
import urllib


def search_url(url):
    """
    >>> search_url("href='aa' value='bb' 'c'")
    ['aa', 'bb']

    >>> search_url("'aa' 'bb'")
    []

    >>> search_url("")
    []
    """

    links = re.findall('''(?:value=|href=)["'](.[^"']+)["']''', url, re.I)
    return links

if __name__ == "__main__":
     with open("links.txt","w") as f:
        for link in search_url(urllib.urlopen('http://kundansingh.com').read()):
            f.write(link + "\n")
    
