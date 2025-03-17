def make_car(manufacturer, model, **options):
    """Construct a dictionary for storing car information.

    Parameters:
        The car's manufacturer.
        The model of the car.
        Additional optional features or details for the car.

    Returns:
        A dictionary containing the car's information, including the manufacturer, model, and any optional features.
    """
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    car_info.update(options)
    return car_info

car1 = make_car('volkswagen', 'GTI', color='gray', tow_package=True)
print(car1)

car2 = make_car('honda', 'odyssey', color='gray', condition='about to fall apart')
print(car2)