# Requisito 10
from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    categories = []
    for new in find_news():
        categories.append(new["category"])

    categories = [
        {"name": name, "quantity": quantity}
        for name, quantity in Counter(categories).items()
    ]
    # print("categories", categories)
    sort = sorted(
        categories,
        key=lambda category: (-category["quantity"], category["name"]))

    categories_sorted_result = [category["name"] for category in sort]
    return categories_sorted_result
