import numpy as np

def pure_python_clip(input_list, min_value, max_value, output_list):
    '''Clip the values in input_list to be between min_value and max_value. Result in output_list
    '''
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    if input_list.shape[0] != output_list.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(input_list.shape[0]):
        output_list[i] = \
            (input_list[i] if input_list[i] < max_value else max_value) \
            if input_list[i] > min_value else min_value

def numpy_clip(input_list, min_value, max_value, output_list):
    np.clip(input_list, min_value, max_value, output_list)
