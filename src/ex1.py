from ValidationException import ValidationException
import csv

class ValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def validate_file(input):
    pass # TODO
    
    with open(input) as file:
        next(file)
        for line_number, line in enumerate(file, start=1):
                try:
                    car, mileage_str = map(str.strip, line.split(','))
                    mileage = int(mileage_str)
                except ValueError:
                    raise ValidationException(f"Invalid mileage: {mileage_str}")
            
def ex1():
    try:
        validate_file("files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()