import requests
import bs4

def request_url(url):
    content = requests.get(url).text
    bs4_object = bs4.BeautifulSoup(content, "html.parser")
    return bs4_object
    

def extract(url, tag, attribute=None):
    content = request_url(url)
    tags = content.find_all(tag)

    if attribute:
        attributes = []
        for tag in tags:
            a = tag.get(attribute)
            if a:
                attributes.append(a)
        return attributes

    return tags
