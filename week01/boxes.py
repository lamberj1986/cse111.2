# Week 1 round 2 practice assignment

import math

no_items = int(input('Enter the number of items: '))
box_max = int(input('Enter the number of items per box: '))

box_math = no_items / box_max
no_boxes = math.ceil(box_math)

print()
print(f'For {no_items} items, packing {box_max} items in each box, you will need {no_boxes} boxes.')