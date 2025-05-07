from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 