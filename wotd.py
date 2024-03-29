from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import os


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error("Error during request to {0} : {1}".format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers["Content-Type"].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print("ERROR:", e)


def getWord():
    raw_html = simple_get('https://www.merriam-webster.com/word-of-the-day')
    soup = BeautifulSoup(raw_html, 'html.parser')
    title = soup.title.text.split()
    return title[4]


def playAgain():
    response = input("Would you like to play again? (y/n)")
    if response.lower() == "y":
        return True
    return False


def clear():
    _ = os.system("cls")
