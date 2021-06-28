import requests

from . import constants


class GoogleBooksSearch:

    def search(self, search_keyword):
        params = {"q": search_keyword}
        response = requests.get(url=constants.GOOGLE_BOOKS_VOLUME_URL, params=params)
        data = response.json()
        result = []
        for book in data.get('items', []):
            id = book.get('id')
            title = book.get('volumeInfo', {}).get('title', '')
            preview_link = book.get('volumeInfo', {}).get('previewLink', '')
            thumbnail = book.get('volumeInfo', {}).get('imageLinks', {}).get('thumbnail', '')
            result.append({'id': id,
                           'title': title,
                           'thumbnail': thumbnail,
                           'previewLink': preview_link})

        return result










    
