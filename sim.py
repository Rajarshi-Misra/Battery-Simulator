from flask import Flask, request, jsonify

app = Flask(__name__)

# Battery state (simulated)
battery = {
    'voltage': 3.7,  # Initial voltage
    'state_of_charge': 100,  # Battery charge percentage (0-100)
    'charging': False,
    'discharging': False
}

@app.route('/battery/control', methods=['POST'])
def control_battery():
    global battery
    data = request.json
    action = data.get('action')

    if action == 'charge':
        battery['charging'] = True
        battery['discharging'] = False
        battery['state_of_charge'] = min(100, battery['state_of_charge'] + 10)
    elif action == 'discharge':
        battery['charging'] = False
        battery['discharging'] = True
        battery['state_of_charge'] = max(0, battery['state_of_charge'] - 10)
    elif action == 'stop':
        battery['charging'] = False
        battery['discharging'] = False
    else:
        return jsonify({'error': 'Invalid action'}), 400

    return jsonify(battery)


@app.route('/battery/status', methods=['GET'])
def status():
    return jsonify(battery)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
