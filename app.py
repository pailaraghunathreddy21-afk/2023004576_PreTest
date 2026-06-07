from flask import Flask, request, jsonify
import heapq
import time

app = Flask(__name__)

# Priority Queue (Min Heap)
vehicle_heap = []

# Priority logic
def get_priority(vehicle_type):
    if vehicle_type == "Emergency":
        return 3
    elif vehicle_type == "Medical":
        return 2
    else:
        return 1

# Add vehicle
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    data = request.json
    
    vehicle_type = data.get("type")
    number = data.get("number")
    
    priority = get_priority(vehicle_type)
    timestamp = time.time()
    
    heapq.heappush(vehicle_heap, (-priority, timestamp, number, vehicle_type))
    
    return jsonify({"message": "Vehicle added successfully"})

# Get top vehicles
@app.route('/get_vehicles', methods=['GET'])
def get_vehicles():
    result = []
    temp = vehicle_heap.copy()
    
    while temp:
        item = heapq.heappop(temp)
        result.append({
            "number": item[2],
            "type": item[3]
        })
    
    return jsonify(result)

@app.route('/')
def home():
    return "Vehicle Scheduler Running"

if __name__ == '__main__':
    app.run(debug=True)