# This is the base class that defines a common action.
class Vehicle:
    """
    A class to represent a generic vehicle.
    All vehicles have a move() method, but the behavior is defined by the subclasses.
    """
    def move(self):
        """
        The base method for a vehicle's movement.
        This is a placeholder that will be overridden by subclasses.
        """
        print("A vehicle is moving.")

# The Car class is a subclass of Vehicle.
class Car(Vehicle):
    """
    A class for a car, inheriting from Vehicle.
    """
    def move(self):
        """
        Overrides the parent's move() method to define how a car moves.
        """
        print("The car is driving 🚗.")

# The Plane class is another subclass of Vehicle.
class Plane(Vehicle):
    """
    A class for a plane, inheriting from Vehicle.
    """
    def move(self):
        """
        Overrides the parent's move() method to define how a plane moves.
        """
        print("The plane is flying ✈️.")

# The Boat class is another subclass of Vehicle.
class Boat(Vehicle):
    """
    A class for a boat, inheriting from Vehicle.
    """
    def move(self):
        """
        Overrides the parent's move() method to define how a boat moves.
        """
        print("The boat is sailing ⛵.")

# This section demonstrates polymorphism in action.
if __name__ == "__main__":
    # Create instances of each subclass.
    my_car = Car()
    my_plane = Plane()
    my_boat = Boat()

    # Call the move() method on each object.
    # The output is different for each object, even though the method call is identical.
    print("--- Demonstrating individual object movement ---")
    my_car.move()
    my_plane.move()
    my_boat.move()

    print("\n--- Demonstrating polymorphism in a list ---")
    # Store the objects in a list.
    vehicles = [my_car, my_plane, my_boat]

    # Iterate through the list and call move() on each object.
    # Python automatically calls the correct move() method for each object type.
    for vehicle in vehicles:
        vehicle.move()
