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

    with open("links.txt","w") as f:
        for link in links:
            f.write(link + "\n")
    return links

if __name__ == "__main__":
    search_url(urllib.urlopen('http://kundansingh.com').read())
