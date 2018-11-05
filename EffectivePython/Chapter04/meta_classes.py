class ValidatePolygon(type):
    def __new__(mcs, name, bases, class_dict):
        # Don't validate the abstract Polygon class
        if bases != (object,):
            print(class_dict)
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(mcs, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # Specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Line(Polygon):
    sides = 1
