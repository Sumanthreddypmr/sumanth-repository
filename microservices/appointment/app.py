from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# In-memory storage for demo purposes
appointments = []

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = next((a for a in appointments if a['id'] == appointment_id), None)
    if appointment:
        return jsonify(appointment)
    return jsonify({'error': 'Appointment not found'}), 404

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointment_id = len(appointments) + 1
    appointment = {'id': appointment_id, **data}
    appointments.append(appointment)
    return jsonify(appointment), 201

@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    data = request.get_json()
    appointment = next((a for a in appointments if a['id'] == appointment_id), None)
    if appointment:
        appointment.update(data)
        return jsonify(appointment)
    return jsonify({'error': 'Appointment not found'}), 404

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    global appointments
    appointments = [a for a in appointments if a['id'] != appointment_id]
    return jsonify({'message': 'Appointment deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)