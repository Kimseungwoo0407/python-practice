import math

class Circle:
    def __init__(self,radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius **2)
    def get_radius(self):
        return self.__radius
    def set_radius(self,value):
        self.__radius = value
    
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        if value <= 0 :
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

print("# 데코레이터를 사용한 getter과 setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2
print("변경된 원의 반지름:", circle.radius)
print()

# 강제로 예외 발생
print("# 강제로 예외를 발생시킵니다.")
circle.radius=-10