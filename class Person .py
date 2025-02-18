class Person :
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Name - {self.name} and Age - {self.age}.")
    p1 = Person("AZ,19")
    p1.greet()