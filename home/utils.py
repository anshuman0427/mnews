import requests
from .models import Articles

def getnews(url):
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('articles'):
            for article in data.get('articles'):
                source = article.get('source').get('name')
                author = article.get('author')
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')
                url_to_image = article.get('urlToImage')
                publishedAt = article.get('publishedAt')
                content = article.get('content')

                # Check if the article already exists to avoid duplicates
                if not Articles.objects.filter(title=title).exists():
                    Articles.objects.create(
                        source=source,
                        author=author,
                        title=title,
                        description=description,
                        url=url,
                        url_to_image=url_to_image,
                        publishedAt=publishedAt,
                        content=content
                    )
    except Exception as e:
        print(e)
