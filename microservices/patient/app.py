from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# In-memory storage for demo purposes
patients = []

@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients)

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = next((p for p in patients if p['id'] == patient_id), None)
    if patient:
        return jsonify(patient)
    return jsonify({'error': 'Patient not found'}), 404

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    patient_id = len(patients) + 1
    patient = {'id': patient_id, **data}
    patients.append(patient)
    return jsonify(patient), 201

@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    patient = next((p for p in patients if p['id'] == patient_id), None)
    if patient:
        patient.update(data)
        return jsonify(patient)
    return jsonify({'error': 'Patient not found'}), 404

@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    global patients
    patients = [p for p in patients if p['id'] != patient_id]
    return jsonify({'message': 'Patient deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)