class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0
    
    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()
    
    def wringOut(self) -> None:
        self.wetness = 0
    
    def isDry(self) -> bool:
        return self.wetness == 0


    def show(self) -> None:
        print(f"{self.color} {self.size} {self.wetness}")

    def __str__(self) -> str:
        return f"{self.color} {self.size} {self.wetness}"
    
def main():
    towel = Towel("", "")
    while True:

        line: str = input() 
        args: list[str] = line.split(" ") 

        if args[0] == "end":
            break
        elif args[0] == "new":
            color: str = args[1]
            size: str = args[2]
            towel = Towel(color, size)
        elif args[0] == "dry":
            amount: int = int(args[1])
            towel.dry(amount)
        elif args[0] == "show":
            print(towel)
        else:
            print("fail: comando não encontrado")
