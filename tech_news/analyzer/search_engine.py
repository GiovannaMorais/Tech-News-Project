from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    searched_news = []
    query = {"title": {"$regex": title, "$options": "i"}}
    for new in search_news(query):
        searched_news.append((new["title"], new["url"]))
    return searched_news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
