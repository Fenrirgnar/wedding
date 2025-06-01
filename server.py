from flask import Flask, request
import requests

app = Flask(__name__)

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' и 'YOUR_CHAT_ID' на ваши данные
TELEGRAM_BOT_TOKEN = '7677636691:AAHVJ-7fUu9vZgV-rqC2i_Lw1ZNMB3dUfMI'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    # Формируем сообщение для отправки в Telegram
    message = f"Новая анкета:\n"
    for key, value in data.items():
        message += f"{key}: {value}\n"

    # Отправляем сообщение в Telegram
    url = f"https://api.telegram.org/bot{T7677636691:AAHVJ-7fUu9vZgV-rqC2i_Lw1ZNMB3dUfMI}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return {"status": "success"}, 200
    else:
        return {"status": "error", "message": response.text}, 500

if __name__ == '__main__':
    app.run(debug=True)
