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

# Outros endpoints da API...

if __name__ == '__main__':
    app.run(debug=True)
