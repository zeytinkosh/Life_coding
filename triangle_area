def calculate_triangle_area(side1, side2, side3):
    """Вычисляет площадь треугольника по трем сторонам"""

    if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
        print('Такого треугольника не существует')

    else:
        sp = (side1 + side2 + side3) / 2
        area = (sp * (sp - side1) * sp * (sp - side2) * sp * (sp - side3)) ** 0.5

        return area


print(calculate_triangle_area(3, 4, 5))
