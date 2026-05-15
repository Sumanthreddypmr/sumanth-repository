from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# In-memory storage for demo purposes
doctors = []

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify(doctors)

@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = next((d for d in doctors if d['id'] == doctor_id), None)
    if doctor:
        return jsonify(doctor)
    return jsonify({'error': 'Doctor not found'}), 404

@app.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.get_json()
    doctor_id = len(doctors) + 1
    doctor = {'id': doctor_id, **data}
    doctors.append(doctor)
    return jsonify(doctor), 201

@app.route('/doctors/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    data = request.get_json()
    doctor = next((d for d in doctors if d['id'] == doctor_id), None)
    if doctor:
        doctor.update(data)
        return jsonify(doctor)
    return jsonify({'error': 'Doctor not found'}), 404

@app.route('/doctors/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    global doctors
    doctors = [d for d in doctors if d['id'] != doctor_id]
    return jsonify({'message': 'Doctor deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)