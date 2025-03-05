from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler
import time, json

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
count = 0

def update_data():
    global count
    
    with open('app.json', 'r') as file:
        data = json.load(file)
    data.append({'count': count, 'message': f'Update happened: {time.strftime("%Y-%m-%d %H:%M:%S")}'})

    with open('app.json', 'w') as file:
        json.dump(data, file)
    count += 1

scheduler.add_job(id = 'Scheduled task', func=update_data, trigger='interval', seconds=30)

@app.route('/data')
def get_data():
    with open('app.json', 'r') as file:
        data = json.load(file)
    
    return jsonify(data)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)