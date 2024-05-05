class Animal:
    def __init__(self, name, species, happy, hungry):
        self.name = name
        self.species = species
        self.happy = happy
        self.hungry = hungry  # 1 = very hungry, 5 = full

    def feed(self, enclosure_dirt_level):
        if enclosure_dirt_level < 5:  # Example threshold for dirt level
            self.hungry -= 2
            self.happy += 1
            if self.happy > 5:
                self.happy = 5
            print("You fed the animal.")
        else:
            print("O recinto está muito sujo para alimentar o animal.")

    def play(self, enclosure_dirt_level):
        if enclosure_dirt_level < 5:  # Example threshold for dirt level
            self.happy += 1
            self.hungry -= 0.5
            if self.happy > 5:
                self.happy = 5
            print("You played with the animal.")
        else:
            print("O recinto está muito sujo para brincar com o animal.")

    def __str__(self):
        return f"{self.name} is a {self.species}. Happy: {self.happy}. Hungry: {self.hungry}"


class Enclosure:
    def __init__(self):
        self.animals = []
        self.dirt_level = 0  # Initialize dirt level

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} foi adicionado ao recinto.")

    def feed_animals(self):
        for animal in self.animals:
            animal.feed(self.dirt_level)  # Pass enclosure dirt level to animal feed method
            if animal.happy > 5:  # Optional: Reset happiness if it exceeds maximum
                animal.happy = 5

    def clean_enclosure(self):
        self.animals = []
        self.dirt_level = 0  # Reset dirt level when cleaning enclosure
        print("O recinto foi limpo.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} foi removido do enclosure.")
        else:
            print(f"{animal.name} não está neste enclosure.")
    
    def calc_visitors(self):
        if not self.animals:
            return 0  # Returns 0 if the enclosure is empty

        happy_total = sum(animal.happy for animal in self.animals)
        happy_avg = happy_total / len(self.animals)

        if happy_avg > 4:
            return 100  # Attracts 100 visitors if the average happiness is high
        elif happy_avg > 2:
            return 50  # Attracts 50 visitors if the average happiness is moderate
        else:
            return 10  # Attracts 10 visitors if the average happiness is low


    def __str__(self):
        return f"Recinto com {len(self.animals)} animais. Nível de sujeira: {self.dirt_level}"
