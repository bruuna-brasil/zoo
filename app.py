from zoo import Animal, Enclosure

if __name__ == "__main__":
    # Criando um animal
    leo = Animal("Leão", "Felino", 80, 50)  # Adicionando o argumento hungry

    # Criando um recinto e adicionando o leão
    enclosure_leoes = Enclosure()
    enclosure_leoes.add_animal(leo)

    # Alimentando o leão
    enclosure_leoes.dirt_level = 4  # Set dirt level below threshold
    leo.feed(enclosure_leoes.dirt_level)

    # Calculando visitantes
    num_visitors = enclosure_leoes.calc_visitors()
    print(f"Número de visitantes: {num_visitors}")
