from pprint import pprint

def build_car_list():
    pass # TODO

    list = []

    with open("files/car-ids.txt", "r") as file1:
        id_model_map = {}
        for line in file1:
            carId,model = map(str.strip,line.split(','))
            id_model_map[int(carId)] = model
        
        
    with open("files/input.txt", "r") as file2:
        next(file2) 
        for line in file2:
            carId, miles = map(str.strip, line.split(','))
            if '.' not in miles:
                if int(carId) in id_model_map:
                    model = id_model_map[int(carId)]
                    list.append({'id': int(carId), 'miles': int(miles), 'model': model})
    return list


def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
