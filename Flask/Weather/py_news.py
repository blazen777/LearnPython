import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except(requests.RequestException, ValueError):
        print("Networking Error")
        return False

def get_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        news_list = soup.find("ul", class_="list-recent-posts").find_all("li")
        result_news = []
        for news in news_list:
            title = news.find("a").text
            link = news.find("a")["href"]
            published = news.find("time").text
            result_news.append({
                "title": title,
                "link": link,
                "published": published,
            })
        return result_news
    return False
