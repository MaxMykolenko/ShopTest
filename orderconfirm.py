from flask import Flask, request, redirect, render_template
import requests

app = Flask(__name__)

@app.route('/')
def order_form():
    return render_template('order_form.html')

@app.route('/order', methods=['POST'])
def order():
    first_name = request.form['first-name']
    middle_name = request.form['middle-name']
    last_name = request.form['last-name']
    quantity = request.form['quantity']

    bot_token = 'YOUR_BOT_TOKEN'  # Заміни на ваш токен бота
    chat_id = 'YOUR_CHAT_ID'  # Заміни на ваш chat_id
    message = f"Новий замовлення:\nІм'я: {first_name}\nПо-Батькові: {middle_name}\nПрізвище: {last_name}\nКількість: {quantity}"

    # Надсилання повідомлення до Telegram
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')
    
    if response.status_code != 200:
        print(f"Помилка при надсиланні повідомлення: {response.status_code}, {response.text}")
    
    return redirect('/confirmation')  # Перенаправлення на сторінку підтвердження

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
