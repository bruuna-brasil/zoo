from flask import Flask, request, jsonify
from zoo import Animal, Enclosure

app = Flask(__name__)
enclosure = Enclosure()

def add_animal():
    data = request.get_json()  # Assume que os dados são enviados como JSON
    if not data:
        return "Dados inválidos", 400

    if len(data) != 4:  # Verifica se os dados estão completos
        return "Dados incompletos", 400

    # Extrai os dados da lista
    name, species, happy, hungry = data

    # Adiciona o animal ao recinto
    animal = Animal(name, species, happy, hungry)
    enclosure.add_animal(animal)

    return "Animal adicionado com sucesso", 200

@app.route('/feed', methods=['POST'])
def feed_animal():
    data = request.get_json()
    name, species, happy, hungry = data
    animal = next((a for a in enclosure.animals if a.name == name), None)
    if animal:
        enclosure.dirt_level = 4
        animal.feed(enclosure.dirt_level)
        return jsonify({'message': f'{name} fed successfully'}), 200
    else:
        return jsonify({'error': 'Animal not found'}), 404

@app.route('/play', methods=['POST'])
def play_with_animal():
    data = request.get_json()
    name, species, happy, hungry = data
    animal = next((a for a in enclosure.animals if a.name == name), None)
    if animal:
        enclosure.dirt_level = 4
        animal.play(enclosure.dirt_level)
        return jsonify({'message': f'{name} played with successfully'}), 200
    else:
        return jsonify({'error': 'Animal not found'}), 404


@app.route('/remove_animal', methods=['POST'])
def remove_animal():
    data = request.get_json()
    name, species, happy, hungry = data
    animal = next((a for a in enclosure.animals if a.name == name), None)
    if animal:
        enclosure.remove_animal(animal)
        return jsonify({'message': f'{name} removed successfully'}), 200
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
