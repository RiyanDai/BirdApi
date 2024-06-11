from flask import Flask, jsonify, request

app = Flask(__name__)

# Muat data burung dari file JSON
import json
with open('birds.json') as f:
    birds = json.load(f)

@app.route('/api/birds', methods=['GET'])
def get_birds():
    return jsonify(birds)

@app.route('/api/birds/by_scientific_name/<string:scientific_name>', methods=['GET'])
def get_bird_by_scientific_name(scientific_name):
    bird = next((bird for bird in birds if bird['scientific_name'] == scientific_name), None)
    if bird:
        return jsonify(bird)
    else:
        return jsonify({'error': 'Bird not found'}), 404

@app.route('/api/birds/by_common_name/<string:common_name>', methods=['GET'])
def get_bird_by_common_name(common_name):
    bird = next((bird for bird in birds if bird['name'].lower() == common_name.lower()), None)
    if bird:
        return jsonify(bird)
    else:
        return jsonify({'error': 'Bird not found'}), 404

@app.route('/api/birds/description/by_scientific_name/<string:scientific_name>', methods=['GET'])
def get_description_by_scientific_name(scientific_name):
    bird = next((bird for bird in birds if bird['scientific_name'] == scientific_name), None)
    if bird:
        return jsonify({'description': bird['description']})
    else:
        return jsonify({'error': 'Bird not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
