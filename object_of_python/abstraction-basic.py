"""
#* 추상화 : abstraction
#* 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
#* 공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.
"""
class Robot:
    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name, number, description,cal1, cal2):
        self.name = name
        self.number = number
        self.description = description
        self.cal1 = cal1
        self.cal2 = cal2
        Robot.population += 1

    # 인스턴스 매서드
    def description(self):
        print(self.description)
    # 인스턴스 매서드
    def add_cal(self):
        return self.cal1 + self.cal2
    # 인스턴스 매서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        print(f"{self.name} die")

    # 클래스 메서드
    @classmethod
    def how_many(cls): #cls 는 클래스를 뜻
        print(f"We have {cls.population} robots.")


