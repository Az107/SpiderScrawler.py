import requests
from bs4 import BeautifulSoup
import json
from colorama import Fore

def downloadWeb(url: str) -> str:
    print("Downloading " + url + "...")
    result =  requests.get(url).text
    print(Fore.WHITE + "[" + Fore.GREEN + "OK" + Fore.WHITE + "]\n")
    return result

def getLinks(html: str) -> list:
    links = []
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def main():
    print("Init SpiderScrawler")


if (__name__ == "__main__"): main()
