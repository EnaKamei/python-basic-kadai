class Human :
  def __init__(self, name , age ):
    self.name = name
    self.age = age

  def check_adult(self):
    if (self.age >= 20):
        print(f"{self.name}は大人です。")  
    else:
        print(f"{self.name}は大人ではありません。")      

human = []
kamei = Human("kamei",26)
human.append(kamei)

sakamoto = Human("sakamoto",53)
human.append(sakamoto)

samurai = Human("samurai",10)
human.append(samurai)

for man in human:
  man.check_adult()