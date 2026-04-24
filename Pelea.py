import random



class description:
    def __init__(self):
        self.name = ""
        self.battery = 150
        self.defense = 100
        self.attack = input("Enter A for attack to " + self.name + " (20-50): ")

    def getname(self):
        return self.name
    def getbattery(self):
        return self.battery
    def getdefense(self):
        return self.defense
    def getattack(self):
        return self.attack
    def setname(self, name):
        self.name = name
    def setbattery(self, battery):
        self.battery = battery
    def setdefense(self, defense):
        self.defense = defense
    def setattack(self, attack):
        self.attack = attack

    def mostrar_Pais(self):
        print("Country: " + str(self.name))
        print("Battery: " + str(self.battery))
        print("Defense: " + str(self.defense))
        print("Attack: " + str(self.attack))

class USA(description):
    def USA_Attack(self, other):
        damage = self.attack - other.defense
        if damage > 0:
            other.battery -= damage
            print(f"{self.name} attacks {other.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack was ineffective against {other.name}!")
    
    def input_attack(self):
        while True:
            try:
                attack_value = int(input(f"Enter A for attack to {self.name} (20-50): "))
                if 20 <= attack_value <= 50:
                    self.attack = attack_value
                    break
                else:
                    print("Please enter a value between 20 and 50.")
            except ValueError:
                print("Invalid input. Please enter a number between 20 and 50.")

    def mostrarUSA(self):
        print("Country: " + str(self.name))
        print("Battery: " + str(self.battery))
        print("Defense: " + str(self.defense))
        print("Attack: " + str(self.attack))

class Venezuela(description):
    def Venezuela_Attack(self, other):
        damage = self.attack - other.defense
        if damage > 0:
            other.battery -= damage
            print(f"{self.name} attacks {other.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack was ineffective against {other.name}!")

def main():
    Usa = USA()
    Usa.setname("USA")
    Usa.setbattery(150)
    Usa.setdefense(100)
    Usa.setattack(random.randint(20, 50))
    Usa.mostrarUSA()
    print()
    Venezuela = Venezuela()
    Venezuela.setname("Venezuela")
    Venezuela.setbattery(170)
    Venezuela.setdefense(50)
    Venezuela.setattack(random.randint(20, 50))
    Venezuela.mostrarVenezuela()
    print()

if __name__ == "__main__":
    main()