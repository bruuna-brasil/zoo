from flask import Flask, request, jsonify
from zoo import Animal, Enclosure

app = Flask(__name__)
enclosure = Enclosure()

@app.route('/add_animal', methods=['POST'])
def add_animal():
    data = request.get_json()
    animal = Animal(data['name'], data['species'], data['happy'], data['hungry'])
    enclosure.add_animal(animal)
    return jsonify({'message': 'Animal added successfully'}), 200

@app.route('/feed', methods=['POST'])
def feed_animal():
    data = request.get_json()
    animal_name = data['name']
    animal = next((a for a in enclosure.animals if a.name == animal_name), None)
    if animal:
        animal.feed()
        return jsonify({'message': f'{animal_name} fed successfully'}), 200
    else:
        return jsonify({'error': 'Animal not found'}), 404

@app.route('/play', methods=['POST'])
def play_with_animal():
    data = request.get_json()
    animal_name = data['name']
    animal = next((a for a in enclosure.animals if a.name == animal_name), None)
    if animal:
        animal.play()
        return jsonify({'message': f'{animal_name} played with successfully'}), 200
    else:
        return jsonify({'error': 'Animal not found'}), 404

@app.route('/remove_animal', methods=['POST'])
def remove_animal():
    data = request.get_json()
    animal_name = data['name']
    animal = next((a for a in enclosure.animals if a.name == animal_name), None)
    if animal:
        enclosure.remove_animal(animal)
        return jsonify({'message': f'{animal_name} removed successfully'}), 200
    else:
        return jsonify({'error': 'Animal not found'}), 404

@app.route('/clean_enclosure', methods=['POST'])
def clean_enclosure():
    enclosure.clean_enclosure()
    return jsonify({'message': 'Enclosure cleaned successfully'}), 200

@app.route('/calc_visitors', methods=['GET'])
def calc_visitors():
    return jsonify({'visitors': enclosure.calc_visitors()}), 200

@app.route('/increase_space', methods=['POST'])
def increase_space():
    data = request.get_json()
    enclosure.increase_space(data['space'])
    return jsonify({'message': 'Space increased successfully'}), 200
    


if __name__ == '__main__':
    app.run(debug=True)
