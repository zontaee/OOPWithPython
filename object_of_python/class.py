# * 객체(object)의 **속성과 행위(methods)**를 하나로 묶고, 구현된 일부를 외부에 감추어 은닉한다.


# ** 사칙연산 계산기


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))


class Cal:

    # 생성자 : 메모리에 올라오는 순간 즉시 실행
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = Cal(1, 2)
print(cal1.a)  # 1
print(cal1.div())  # 0.5
