from sense_hat import SenseHat
sense = SenseHat()


def get_temperature():
    temp = sense.get_temperature()
    return round(temp, 1)


def cooler_turn_on():
    cooler_color = (0, 0, 255)
    for i in range(8):
        sense.set_pixel(0, i, cooler_color)


def cooler_turn_off():
    cooler_color = (0, 0, 0)
    for i in range(8):
        sense.set_pixel(0, i, cooler_color)


def heater_turn_on():
    heater_color = (255, 0, 0)
    for i in range(8):
        sense.set_pixel(7, i, heater_color)


def heater_turn_off():
    heater_color = (0, 0, 0)
    for i in range(8):
        sense.set_pixel(7, i, heater_color)


def cooler_turn_on_test():
    cooler_color = (0, 255, 255)
    for i in range(8):
        sense.set_pixel(1, i, cooler_color)


def cooler_turn_off_test():
    cooler_color = (0, 0, 0)
    for i in range(8):
        sense.set_pixel(1, i, cooler_color)


def heater_turn_on_test():
    heater_color = (255, 100, 0)
    for i in range(8):
        sense.set_pixel(6, i, heater_color)


def heater_turn_off_test():
    heater_color = (0, 0, 0)
    for i in range(8):
        sense.set_pixel(6, i, heater_color)
