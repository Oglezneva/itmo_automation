# ЗАДАЧА 1
# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def square(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# object1 = Rect(6, 4)
# object2 = Rect(8, 2)
# object3 = Rect(15, 11)
#
#
# print(object1.square())
# print(object2.perimeter())
# print(object3.perimeter())

# ЗАДАЧА 2
# class Math:
#     def __init__(self, a, b):
#      self.a = a
#      self.b = b
#
#     def addition(self):
#         print(self.a + self.b)
#     def multiplication(self):
#         print(self.a * self.b)
#     def division(self):
#         print(self.a / self.b)
#     def subtraction(self):
#         print(self.a - self.b)
#
# object1 = Math(2, 4)
#
# object1.addition()
# object1.multiplication()
# object1.division()
# object1.subtraction()

# ЗАДАЧА 3
class Button:

    def __init__(self, text, type, loc):
       self.text = text
       self.type = type
       self.loc = loc

    def click(self):
        return 'Клик по кнопке - {}'.format(self.text)


item_0 = Button('Text box', 'Кнопка', '')
item_1 = Button('Check box', 'Кнопка', '')
item_2 = Button('Radio Button', 'Кнопка', '' )
item_3 = Button('Web tables', 'Кнопка', '' )
item_4 = Button('Buttons', 'Кнопка', '' )
item_5 = Button('Links', 'Кнопка', '' )
item_6 = Button('Broken Links - Images', 'Кнопка', '' )
item_7 = Button('Upload and Download', 'Кнопка', '')
item_8 = Button('Dynamic Properties', 'Кнопка', '' )

print(item_0.click())
print(item_1.click())
print(item_2.click())
print(item_3.click())
print(item_4.click())
print(item_5.click())
print(item_6.click())
print(item_7.click())
print(item_8.click())