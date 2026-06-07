from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

vehicles = []
tasks = []

# Home route (check server)
@app.route('/')
def home():
    return "Vehicle Maintenance Scheduler Running"

# Add Vehicle
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    data = request.json
    vehicles.append(data)
    return jsonify({"message": "Vehicle added successfully"})

# Add Task
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({"message": "Task added successfully"})

# Check Schedule
@app.route('/schedule', methods=['GET'])
def schedule():
    today = datetime.now()
    result = []

    for v in vehicles:
        last_date = datetime.strptime(v['last_service_date'], "%Y-%m-%d")

        for t in tasks:
            next_service = last_date + timedelta(days=t['interval_days'])

            if next_service <= today:
                result.append({
                    "vehicle_id": v['vehicle_id'],
                    "task": t['task_name'],
                    "status": "Due"
                })

    return jsonify(result)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
    