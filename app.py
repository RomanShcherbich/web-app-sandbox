from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz
import requests

# Загрузка переменных окружения
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/time')
def get_time():
    tbilisi_tz = pytz.timezone('Asia/Tbilisi')
    portugal_tz = pytz.timezone('Europe/Lisbon')
    
    tbilisi_time = datetime.now(tbilisi_tz).strftime('%H:%M:%S')
    portugal_time = datetime.now(portugal_tz).strftime('%H:%M:%S')
    
    return jsonify({
        "tbilisi": tbilisi_time,
        "portugal": portugal_time
    })

@app.route('/api/currency')
def get_currency():
    try:
        # Используем бесплатный API для получения курсов валют
        response = requests.get('https://open.er-api.com/v6/latest/USD')
        data = response.json()
        
        if data['result'] == 'success':
            return jsonify({
                'usd_to_eur': data['rates']['EUR'],
                'timestamp': data['time_last_update_utc']
            })
        else:
            return jsonify({'error': 'Failed to fetch currency rates'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 