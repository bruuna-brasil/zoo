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
    def __init__(self, initial_space=30):
        self.animals = []
        self.space = initial_space  # Inicialmente, cada recinto tem 30 metros quadrados

    def add_animal(self, animal):
        if len(self.animals) * 30 >= self.space:
            print("Não há espaço suficiente para adicionar este animal.")
        else:
            self.animals.append(animal)
            print(f"{animal.name} foi adicionado ao enclosure.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} foi removido do enclosure.")
        else:
            print(f"{animal.name} não está neste enclosure.")

    def clean_enclosure(self):
        self.animals = []
        print("O enclosure foi limpo.")

    def calc_visitors(self):
        if not self.animals:
            return 0  # Retorna 0 se o enclosure estiver vazio

        happy_total = sum(animal.happy for animal in self.animals)
        happy_avg = happy_total / len(self.animals)

        if happy_avg > 4:
            return 100  # Atrai 100 visitantes se a felicidade média for alta
        elif happy_avg > 2:
            return 50  # Atrai 50 visitantes se a felicidade média for moderada
        else:
            return 10  # Atrai 10 visitantes se a felicidade média for baixa

    def increase_space(self, additional_space):
        self.space += additional_space
        print(f"O espaço do enclosure foi aumentado para {self.space} metros quadrados.")


    def __str__(self):
        return f"Recinto com {len(self.animals)} animais. Nível de sujeira: {self.dirt_level}"
