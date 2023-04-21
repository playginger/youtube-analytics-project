import requests
import os


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_info = []
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.get_channel_info()
        print(f"Название канала: {channel_info['title']}")
        print(f"Описание канала: {channel_info['description']}")
        print(f"Количество подписчиков: {channel_info['subscriberCount']}")

    def get_channel_info(self) -> dict:
        """Запрос к API и получение информации о канале в виде словаря."""
        apikey = os.environ.get('YT_API_KEY')
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_info}&key={apikey}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            channel_info = {
                'title': data['items'][0]['snippet']['title'],
                'description': data['items'][0]['snippet']['description'],
                'subscriberCount': data['items'][0]['statistics']['subscriberCount']
            }
            return channel_info
        else:
            print("Ошибка при запросе к API")
            return {}
