class Base:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Base.show_info: Name = {self.name}")

    def action(self):
        print("Base.action: Performing base action")


class Derived(Base):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def show_info(self):
        # Override method
        print(f"Derived.show_info: Name = {self.name}, Value = {self.value}")

    def derived_action(self):
        print(f"Derived.derived_action: Value squared = {self.value ** 2}")


# --- Test Program ---

if __name__ == "__main__":
    print("--- Testing Base Class ---")
    b = Base("BaseObject")
    b.show_info()
    b.action()

    print("\n--- Testing Derived Class ---")
    d = Derived("DerivedObject", 5)
    d.show_info()        # overridden method
    d.action()           # inherited method
    d.derived_action()   # method of derived class
