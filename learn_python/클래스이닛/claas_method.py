

class item:
    def __init__(self, name, price, weight, isdropable):
        self.name= name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def selling(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}을 버렸습니다]")
        else:
            print(f"[{self.name}을 버릴 수 없습니다.]")
        

class Wearableitem(item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}] 착용했습니다. {self.effect}")
    
class Usableitme(item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"[{self.name}] 사용했습니다. {self.effect}가 지속됩니다.")
        

# 인스턴스 생성
sword = Wearableitem("이응", 3000, 3.5, True, "체력 300증가")
sword.wear()
sword.discard()
