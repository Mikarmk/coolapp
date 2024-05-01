import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def get_all_internal_links(url, visited=set()):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(response.url))
        links = set()
        for tag in soup.find_all('a', href=True):
            href = tag.attrs['href']
            full_url = urljoin(base_url, href)
            if base_url in full_url and full_url not in visited:
                links.add(full_url)
        return links
    except requests.RequestException as e:
        print(f'Error while requesting {url}: {e}')
        return set()

def find_errors_and_parse(url, visited):
    errors = []
    internal_links = get_all_internal_links(url, visited)
    for link in internal_links:
        if link not in visited:
            visited.add(link)
            print(f'Checking {link}')
            # Вставь сюда свою логику поиска ошибок, и добавь их к списку ошибок
            # Пример ошибки для демонстрации
            errors.append((link, 'Пример ошибки'))
            errors.extend(find_errors_and_parse(link, visited))
    return errors

initial_url = 'тут ссылка на сайт'

visited_urls = set()
all_errors = find_errors_and_parse(initial_url, visited_urls)

for error_url, error in all_errors:
    print(f'Error on page {error_url}: {error}')
