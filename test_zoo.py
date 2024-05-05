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

if __name__ == '__main__':
    unittest.main()
