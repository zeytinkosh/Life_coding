import requests


def send_telegram_message():

    api_key = "6576223609:AAFyKRhiBQzQvcoeL0-h-FbjBG8XFdOhe-s"
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'

    param = {
        "chat_id": chat_id,
        "text": f'Привет! Время выполнить ПРИВЫЧКУ в МЕСТЕ'
    }

    print(requests.get(url, param).json())


send_telegram_message()
