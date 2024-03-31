import requests


def get_telegram_chat_id():
    TOKEN = "your_token"
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

    response = requests.get(url).json()

    if 'result' in response and response['result']:
        chat_id = response['result'][0]['message']['chat']['id']
        return chat_id
    else:
        print("Невозможно получить chat ID.")
        return None


print(get_telegram_chat_id())



#def send_telegram_message():
#
#    api_key = "6576223609:AAFyKRhiBQzQvcoeL0-h-FbjBG8XFdOhe-s"
#
#    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
#
#    param = {
#        "chat_id": 332689919,
#        "text": f'Привет! Время выполнить ПРИВЫЧКУ в МЕСТЕ'
#    }
#
#    print(requests.get(url, param).json())
#
#
#send_telegram_message()
