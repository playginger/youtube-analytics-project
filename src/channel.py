import requests
import os
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, info: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.channel = info.get_channel_info(self.channel_id)
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscriberCount = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.views_count = int(self.channel['items'][0]['statistics']['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.get_channel_info()
        print(f"id канала: {channel_info['id']}")
        print(f"Название канала: {channel_info['title']}")
        print(f"Описание канала: {channel_info['description']}")
        print(f"количество видео: {channel_info['video_count']}")
        print(f"количество просмотров: {channel_info['views_count']}")
        print(f"Количество подписчиков: {channel_info['subscriberCount']}")
        print(f"ссылка на канал: {channel_info['url']}")

    def get_channel_info(self) -> dict:
        """Запрос к API и получение информации о канале в виде словаря."""
        apikey = os.environ.get('API_KEY')
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={apikey}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            channel_info = {
                'id': data['items'][0]['snippet']['id'],
                'title': data['items'][0]['snippet']['title'],
                'description': data['items'][0]['snippet']['description'],
                'video_count': data['items'][0]['snippet']['video_count'],
                'views_count': data['items'][0]['snippet']['views_count'],
                'subscriberCount': data['items'][0]['statistics']['subscriberCount'],
                'url': f'https://www.youtube.com/channel/{self.channel_id}'
            }
            return channel_info
        else:
            print("Ошибка при запросе к API")
            return {}

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def channel_id(self):
        return self.channel_id

    def to_json(self, filename):
        channel_dict = {"id": self.channel_id,
                        "title": self.title,
                        "video_count": self.video_count,
                        "url": self.url,
                        "description": self.description,
                        "subscriberCount": self.subscriberCount,
                        "views_count": self.views_count
                        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(channel_dict, f, indent=2, ensure_ascii=False)

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
