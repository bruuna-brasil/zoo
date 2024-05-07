import unittest
from zoo import Animal, Enclosure

class TestAnimal(unittest.TestCase):
    def test_create_animal(self):
        animal = Animal("Leão", "Felino", 4, 3)
        self.assertEqual(animal.name, "Leão")
        self.assertEqual(animal.species, "Felino")
        self.assertEqual(animal.happy, 4)
        self.assertEqual(animal.hungry, 3)

    def test_feed(self):
        animal = Animal("Leão", "Felino", 4, 3)
        enclosure = Enclosure()  # Create an enclosure for testing
        enclosure.dirt_level = 4  # Set dirt level below threshold
        animal.feed(enclosure.dirt_level)
        self.assertEqual(animal.happy, 5)  # Happiness should increase by 1
        self.assertEqual(animal.hungry, 1)  # Hunger should decrease by 2

        enclosure.dirt_level = 6  # Set dirt level above threshold
        animal.feed(enclosure.dirt_level)
        self.assertEqual(animal.happy, 5)  # Happiness should remain the same
        self.assertEqual(animal.hungry, 1)  # Hunger should remain the same

    def test_play(self):
        animal = Animal("Leão", "Felino", 4, 3)
        enclosure = Enclosure()  # Create an enclosure for testing
        enclosure.dirt_level = 4  # Set dirt level below threshold
        animal.play(enclosure.dirt_level)
        self.assertEqual(animal.happy, 5)  # Happiness should increase by 1
        self.assertEqual(animal.hungry, 2.5)  # Hunger should decrease by 0.5

        enclosure.dirt_level = 6  # Set dirt level above threshold
        animal.play(enclosure.dirt_level)
        self.assertEqual(animal.happy, 5)  # Happiness should remain the same
        self.assertEqual(animal.hungry, 2.5)  # Hunger should remain the same

class TestEnclosure(unittest.TestCase):
    def test_add_animal(self):
        enclosure = Enclosure()
        animal = Animal("Leão", "Felino", 4, 3)
        enclosure.add_animal(animal)
        self.assertIn(animal, enclosure.animals)  # Animal should be in the enclosure's list of animals

    def test_remove_animal(self):
        enclosure = Enclosure()
        animal = Animal("Leão", "Felino", 4, 3)
        enclosure.add_animal(animal)
        enclosure.remove_animal(animal)
        self.assertNotIn(animal, enclosure.animals)  # Animal should not be in the enclosure after removal

    def test_clean_enclosure(self):
        enclosure = Enclosure()
        animal = Animal("Leão", "Felino", 4, 3)
        enclosure.add_animal(animal)
        enclosure.clean_enclosure()
        self.assertEqual(len(enclosure.animals), 0)  # Enclosure should be empty after cleaning

    def test_calc_visitors(self):
        enclosure = Enclosure()
        num_visitors = enclosure.calc_visitors()
        self.assertEqual(num_visitors, 0)  # Number of visitors should be 0 if there are no animals in the enclosure

    def test_increase_space(self):
        enclosure = Enclosure(initial_space=30)  # Create an enclosure with initial space of 30 square meters
        animal1 = Animal("Leão", "Felino", 4, 3)
        animal2 = Animal("Tigre", "Felino", 4, 3)
        enclosure.add_animal(animal1)
        enclosure.add_animal(animal2)

        enclosure.increase_space(60)  # Increase space to 90 square meters
        self.assertIn(animal1, enclosure.animals)  # Animal 1 should still be in the enclosure
        self.assertNotIn(animal2, enclosure.animals)  # Animal 2 should not be in the enclosure anymore

        animal3 = Animal("Pantera", "Felino", 4, 3)
        enclosure.add_animal(animal3)
        self.assertIn(animal3, enclosure.animals)  # Animal 3 should now be added as there is enough space


if __name__ == '__main__':
    unittest.main()


# testes de sistema 

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
    visitors, money_earned = enclosure_leoes.calc_visitors()

    print(f"Número de visitantes: {visitors} Dinheiro arrecadado: {money_earned}")
