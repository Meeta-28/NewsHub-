import requests
import time
from django.shortcuts import render
from news.models import Article


def get_news(api_key, category=None, search_query=None):
    if search_query:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": search_query,
            "sortBy": "publishedAt",
            "apiKey": api_key,
            "t": int(time.time())
        }
    else:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": "in",
            "apiKey": api_key,
            "t": int(time.time())
        }
        if category:
            params["category"] = category

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        article_data = []
        for article in articles:
            title = article.get("title", "")
            summary = article.get("description", "") or ""
            img_url = article.get("urlToImage", "") or ""
            source_url = article.get("url", "")
            source_name = article.get("source", {}).get("name", "")
            article_data.append({
                "title": title,
                "summary": summary,
                "img_url": img_url,
                "source_url": source_url,
                "source_name": source_name
            })
            
            # Save the article data in the database
            article_obj = Article.objects.create(
                title=title,
                summary=summary,
                img_url=img_url,
                source_url=source_url,
                source_name=source_name
            )
            article_obj.save()

        return article_data
    else:
        print("Error: unable to retrieve news data")
        return []

def home(request):
    api_key = "02fb8889dda649939204a277d49190f1"
    category = request.POST.get('category')
    search_query = request.POST.get('search_query')

    if not search_query:
        if category:
            article_data = Article.objects.filter(source_name=category)[:3]
        else:
            article_data = Article.objects.all()[:3]
    else:
        article_data = Article.objects.filter(title__icontains=search_query)[:3]

    context = {
        'article_data': article_data,
        'category': category,
        'search_query': search_query
    }
    return render(request, 'news.html', context)



'''import requests
import time

def get_news(api_key, category=None):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": api_key,
        "t": int(time.time())
    }
    if category:
        params["category"] = category
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        article_data = []
        for article in articles:
            title = article.get("title", "")
            summary = article.get("description", "")
            img_url = article.get("urlToImage", "")
            source_url = article.get("url", "")
            source_name = article.get("source", {}).get("name", "")
            article_data.append({
                "title": title,
                "summary": summary,
                "img_url": img_url,
                "source_url": source_url,
                "source_name": source_name
            })
        return article_data
    else:
        print("Error: unable to retrieve news data")
        return []

def home(request):
    api_key = "867c7153fcb343d09a392e9a7548e172"
    category = request.POST.get('category')  # no default category
    article_data = get_news(api_key, category)

    # If the selected category has less than 3 articles, get additional articles from the "general" category
    if len(article_data) < 3 and category != "general":
        general_data = get_news(api_key, "general")
        article_data.extend(general_data[:3-len(article_data)])

    context = {
        'article_data': article_data,
        'category': category
    }
    return render(request, 'news.html', context)'''






