import math

def circle(x: list, x0: float, y0: float, r: float) -> list:
    """Returns all the y coordinates of a circle at locations x given a center x0, y0 and a radius r"""
    positive_y_coords = []
    negative_y_coords = []
    for x_coord in x:
        # (x-x0)^2 + (y-y0)^2 = r^2
        # (y-y0)^2 = r^2 - (x-x0)^2
        # y-y0 = (r + (x-x0))(r - (x-x0))
        # y = (r + (x-x0))(r - (x-x0)) + y0
        # or, y = sqrt(r^2 - (x-x0)^2) + y0
        positive_y_coords.append(math.sqrt(r**2 - (x_coord - x0)**2) + y0)
        negative_y_coords.append(-math.sqrt(r**2 - (x_coord - x0)**2) + y0)
    return positive_y_coords, negative_y_coords

def order_array(input_array):
    """Returns an array of numbers sorted from smaller to larger given an input array of numbers"""
    temp_array = input_array.copy()
    is_sorted = False
    while not is_sorted:
        is_sorted = True # if all the elements are in order, then we are sorted by default
        for i in range(len(temp_array) - 1): # go over all the elements
            if temp_array[i] > temp_array[i+1]: # not in order?
                temp_num = temp_array[i]
                temp_array[i] = temp_array[i+1] # bump the smaller number down
                temp_array[i+1] = temp_num # make the next one the larger number
                is_sorted = False
    return temp_array
            