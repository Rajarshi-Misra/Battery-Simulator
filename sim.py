from flask import Flask, jsonify

app = Flask(__name__)

# In-memory data for batteries
batteries = {
    1: {"capacity": 50},  # Battery 1 starts at 50%
    2: {"capacity": 75},  # Battery 2 starts at 75%
    # Add more batteries as needed
}

# Route to get the current charge for a battery
@app.route("/<int:battery_id>/get", methods=["GET"])
def get_battery_charge(battery_id):
    battery = batteries.get(battery_id)
    if not battery:
        return jsonify({"error": "Battery not found"}), 404
    return jsonify({"battery_id": battery_id, "charge": battery["capacity"]})

# Route to increase battery charge by 1%
@app.route("/<int:battery_id>/charge", methods=["POST"])
def increase_battery_charge(battery_id):
    battery = batteries.get(battery_id)
    if not battery:
        return jsonify({"error": "Battery not found"}), 404
    if battery["capacity"] >= 100:
        return jsonify({"error": "Battery fully charged"}), 400
    
    battery["capacity"] = min(100, battery["capacity"] + 1)
    return jsonify({"battery_id": battery_id, "charge": battery["capacity"]})

# Route to decrease battery charge by 1%
@app.route("/<int:battery_id>/discharge", methods=["POST"])
def decrease_battery_charge(battery_id):
    battery = batteries.get(battery_id)
    if not battery:
        return jsonify({"error": "Battery not found"}), 404
    if battery["capacity"] <= 0:
        return jsonify({"error": "Battery fully discharged"}), 400
    
    battery["capacity"] = max(0, battery["capacity"] - 1)
    return jsonify({"battery_id": battery_id, "charge": battery["capacity"]})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
