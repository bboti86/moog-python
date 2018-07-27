from time import sleep
import requests
from bs4 import BeautifulSoup
import urllib


def continue_crawl(search_history, target_url, max_steps=25):
    """
    this function will decide if the crawling should continue or not
    """

    print("{}. Now crawling: {}".format(len(search_history), search_history[-1]))
    if target_url in search_history:
        # stop if target_url is reached already
        print("target reached")
        return False
    elif len(search_history) > max_steps:
        # stop after 25 hops
        print("too many hops")
        return False
    elif len(search_history) == 0:
        # empty history means first url
        print("first url")
        return True
    elif search_history[-1] in search_history[:-1]:
        # stop if reached a loop
        print("loop detected")
        return False
    else:
        print("continue")
        # continune in any other case
        return True


def find_first_link(url):
    """
    This function is responsible for fethcing the page and
    finding the first link on the webpage.
    """
    # get the HTML from "url", use the requests library
    response = requests.get(url)
    html = response.text
    # feed the HTML into Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # find the first link in the article
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    # return the first link as a string, or return None if there is no link
    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None
    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

# list of articles visited
article_chain = [start_url]
while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article_chain
    article_chain.append(first_link)
    # delay for about two seconds
    sleep(1)
