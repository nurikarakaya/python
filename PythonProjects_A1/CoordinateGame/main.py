from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_in_rectangle(self, corner1, corner2):
        """ accepts two points and assumes a rectangle drawn from the corners,
        and checks if the point falls into the rectangle"""
        if corner1.x < self.x < corner2.x and corner1.y < self.y < corner2.y:
            return True
        return False

    def is_in_rectangle_2(self, some_rectangle):
        """ accepts a rectangle, and checks if the point falls into the rectangle"""
        corner1 = some_rectangle.corner_1
        corner2 = some_rectangle.corner_2
        if corner1.x < self.x < corner2.x and corner1.y < self.y < corner2.y:
            return True
        return False

    def distance(self, other_point):
        """accepts another point, and returns the distance between two points"""
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, corner_1, corner_2):
        self.corner_1 = corner_1
        self.corner_2 = corner_2

    def area_of_rectangle(self):
        return abs(self.corner_1.x - self.corner_2.x) * abs(self.corner_1.y - self.corner_2.y)


my_rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))

print("The rectangle coordinates are (", my_rectangle.corner_1.x, ",", my_rectangle.corner_1.y, ") and ",
      my_rectangle.corner_2.x, ",", my_rectangle.corner_2.y, ")")

user_guess = Point(float(input("enter a coordinate for x: ")), float(input("enter a coordinate for y: ")))
user_guess_area = int(input("guess the area of the rectangle: "))
area_of_rectangle = my_rectangle.area_of_rectangle()

print("you guessed the are correctly, it is ", area_of_rectangle) if (int(area_of_rectangle) == user_guess_area) \
    else print("you were wrong the area of the rectangle is ", area_of_rectangle)
print("the point is inside the rectangle") if user_guess.is_in_rectangle_2(my_rectangle) \
    else (print("the point is NOT inside the rectangle"))
