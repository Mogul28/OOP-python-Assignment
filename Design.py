# This is the base class for all superheroes.
# It represents the foundational attributes and behaviors common to all of them.
class Superhero:
    """
    A class to represent a generic superhero.

    Attributes:
        name (str): The superhero's alias.
        secret_identity (str): The superhero's civilian name.
        power (str): The superhero's primary ability.
        health (int): The current health of the superhero, defaults to 100.
        is_good (bool): True if the superhero is good, False otherwise.
    """
    
    # The constructor method, used to initialize each new Superhero object.
    # It takes unique values for name, secret_identity, and power.
    def __init__(self, name: str, secret_identity: str, power: str, is_good: bool, health: int = 100):
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.is_good = is_good
        self.health = health
        print(f"{self.name}, the hero with the power of {self.power}, has been created!")

    # A method to describe the use of the superhero's power.
    def use_power(self):
        print(f"{self.name} unleashes their {self.power}!")
    
    # A method to decrease the superhero's health.
    def take_damage(self, damage_amount: int):
        self.health -= damage_amount
        print(f"{self.name} takes {damage_amount} damage! Current health: {self.health}")
    
    # A method to check if the superhero is still alive.
    def is_alive(self) -> bool:
        return self.health > 0

# The subclass, representing a more specific type of superhero.
# It inherits from the Superhero class, getting all its attributes and methods.
class FlyingSuperhero(Superhero):
    """
    A class representing a flying superhero, inheriting from the Superhero class.

    Attributes:
        flight_speed (int): The superhero's top flight speed in miles per hour.
    """
    
    # The constructor for the subclass. We call the parent's constructor using super()
    # to handle the common attributes, and then add our new, specific attribute.
    def __init__(self, name: str, secret_identity: str, power: str, is_good: bool, flight_speed: int):
        # Call the parent class's constructor
        super().__init__(name, secret_identity, power, is_good)
        self.flight_speed = flight_speed
        print(f"{self.name} can fly at speeds up to {self.flight_speed} mph.")
        
    # This method overrides the parent's `use_power` method.
    # This is an example of polymorphism, where a method has a different behavior in the subclass.
    def use_power(self):
        print(f"{self.name} soars into the sky at {self.flight_speed} mph, using their power of {self.power}!")

# --- Demonstration of the Classes ---
if __name__ == "__main__":
    print("--- Creating a standard superhero ---")
    hero_one = Superhero("The Sentinel", "Alex Rayner", "super strength", True)
    hero_one.use_power()
    hero_one.take_damage(20)
    print(f"Is {hero_one.name} alive? {hero_one.is_alive()}\n")

    print("--- Creating a flying superhero ---")
    flying_hero = FlyingSuperhero("Skylark", "Jane Doe", "aerokinesis", True, 250)
    # This call uses the overridden method from the subclass.
    flying_hero.use_power() 
    flying_hero.take_damage(50)
    
    # We can still use methods from the parent class.
    print(f"Is {flying_hero.name} alive? {flying_hero.is_alive()}")
    
    # An example of a villain (a bad superhero).
    print("\n--- Creating a supervillain ---")
    villain = Superhero("Shadow", "Unknown", "darkness manipulation", False)
    villain.use_power()
