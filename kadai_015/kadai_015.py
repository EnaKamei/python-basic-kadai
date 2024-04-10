class Human:
    def __init__(self):
        self.name = ""

    def set_info(self, name , age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"私の名前は{self.name}で{self.age}歳です。")

me = Human()

me.set_info("亀井","26")
me.print_info()


#或いは下記。
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"私の名前は{self.name}で{self.age}歳です。")

me = Human("亀井","26")

me.print_info()