import requests
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
        response = response.json()

        money = request.form.get('money')
        rates = request.form.get('rates')

        if rates == '1':
            total = float(money) * response['rates']['USD']
            total = str(round(total, 2)) + ' $'
            return render_template('index.html', total=total)
        if rates == '2':
            total = float(money) * response['rates']['EUR']
            total = str(round(total, 2)) + ' €'
            return render_template('index.html', total=total)
        if rates == '3':
            total = float(money) * response['rates']['CNY']
            total = str(round(total, 2)) + ' ¥'
            return render_template('index.html', total=total)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

