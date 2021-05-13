import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    arr = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    for axis in [0, 1, None]:
        calculations['mean'].append(np.mean(arr, axis=axis).tolist())

    for axis in [0, 1, None]:
        calculations['variance'].append(np.var(arr, axis=axis).tolist())

    for axis in [0, 1, None]:
        calculations['standard deviation'].append(
            np.std(arr, axis=axis).tolist())

    for axis in [0, 1, None]:
        calculations['max'].append(np.amax(arr, axis=axis).tolist())

    for axis in [0, 1, None]:
        calculations['min'].append(np.amin(arr, axis=axis).tolist())

    for axis in [0, 1, None]:
        calculations['sum'].append(np.sum(arr, axis=axis).tolist())

    return calculations
