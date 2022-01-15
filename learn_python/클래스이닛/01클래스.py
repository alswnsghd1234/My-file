champ_name = '개새끼'
champ_health = 900
champ_attack = 400

print(f"{champ_name}님 꺼지세요")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")
    
basic_attack(champ_name,champ_attack)

print("------------------------")

class champ:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사 협곡에서 제발 꺼지세요")
    def basic_attack(self):
        print(f"{self.name} 기본공격!! {self.attack}")

korean = champ("짜장맨",900,400)
English = champ("양키",400,300)

korean.basic_attack()
English.basic_attack()
champ("짜장맨",900,400)
print(korean)

if __name__ == "__main__":
    print(champ(name, health, attack))

        
        
