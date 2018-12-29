class Building:

    # тип здания
    building_type = None

    def __init__(self, floors, material):
        # Количество этажей
        self.floors = floors
        self.material = material

    def get_info(self):
        print("Это здание высотой в " + str(self.floors) + " этажей")
        print("Это здание из " + self.material)
        print("Тип здания" + self.building_type)


class Stadion(Building):
    # тип здания
    building_type = "Стадион"

    def __init__(self, capacity, floors, working_hours):
        self.material = "Бетон"
        self.capacity = capacity;
        self.floors = floors;
        self.working_hours = working_hours;

    def get_info(self):
        print("Это здание высотой в " + str(self.floors) + " этажей")
        print("Это здание из " + self.material)
        print("Тип здания" + self.building_type)
        print("Вместимость стадиона " + str(self.capacity))
        print("Часы работы" + self.working_hours)

    def get_in_condition(self):
        return "Билет"

class SwimmingPool(Building):
    # Тип здания
    building_type = "Бессейн"

    def __init__(self, floors, working_hours, depth, length, tracks_count):
        self.material = ["Металл", "Кирпич"]
        self.floors = floors
        self.working_hours = working_hours
        self.depth = depth
        self.length = length
        self.tracks_count = tracks_count

    def get_info(self):
        print("Это здание высотой в " + str(self.floors) + " этажей")
        print("Это здание из " + self.material)
        print("Тип здания" + self.building_type)
        print("Характеристики бассейна " + str(self.depth) + ", " + str(self.lengh) + ", " + str(self.tracks_count))
        print("Часы работы" + self.working_hours)

    def get_in_condition(self):
         return "Абонемент + Справка"



