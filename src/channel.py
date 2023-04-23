import googleapiclient
import requests
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_info = []
        self.channel_id = channel_id
        self.api_key = os.environ.get('API_KEY')

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.get_channel_info()
        print(f"Название канала: {channel_info['title']}")
        print(f"Описание канала: {channel_info['description']}")
        print(f"Количество подписчиков: {channel_info['subscriberCount']}")

    def get_channel_info(self) -> dict:
        """Запрос к API и получение информации о канале в виде словаря."""
        apikey = os.environ.get('API_KEY')
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={apikey}"
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

    @classmethod
    def get_service(cls, api_key: str) -> 'googleapiclient.discovery.Resource':
        credentials = Credentials.from_authorized_user_info(info=None)
        service = build('youtube', 'v3', developerKey=api_key, credentials=credentials)
        return service

    def to_json(self, file_path: str) -> None:
        with open(file_path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)


if __name__ == '__main__':
    channel_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'
    api_key = os.environ.get('API_KEY')
    vdud = Channel(channel_id, )
    vdud.print_info()
