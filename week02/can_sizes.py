import math
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(dir_path, 'cans.csv')

radius = 0.0
height = 0.0

def main():
    # do something
    with open(filename) as data_list:
        next(data_list) # Skips firt line of the file
        for line in data_list:
            parts = line.split(',')
            can_name = parts[0]
            can_radius = float(parts[1])
            can_height = float(parts[2])
            can_cost = parts[3]

            volume = compute_volume(can_radius,can_height)
            surface_area = compute_surface_area(can_radius, can_height)

            can_efficiency = compute_storage_efficiency(volume, surface_area)

            print(f'{can_name} {can_efficiency:.2f}')

def compute_volume(radius, height):
    # do something
    volume = math.pi * (radius ** 2)* height
    return volume

def compute_surface_area(radius, height):
    # do something
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency

main()