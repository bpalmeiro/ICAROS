import numpy as np
from datetime import datetime
from   typing      import Tuple, List
from . kr_types    import Number
from numpy import pi

def phirad_to_deg(r : float)-> float:
    return (r + pi) * 180 / pi

def time_delta_from_time(ts):
    dt = [(datetime.fromtimestamp(ts[i]) - datetime.fromtimestamp(ts[0])).total_seconds()
            for i in range (len(ts))]
    return np.array(dt)


def find_nearest(array : np.array, value : Number)->Number:
    """Return the array element nearest to value"""
    idx = (np.abs(array-value)).argmin()
    return array[idx]


def divide_np_arrays(num : np.array, denom : np.array) -> np.array:
    """Safe division of two arrays"""
    assert len(num) == len(denom)
    ok    = denom > 0
    ratio = np.zeros(len(denom))
    np.divide(num, denom, out=ratio, where=ok)
    return ratio


def file_numbers_from_file_range(file_range : Tuple[int, int])->List[str]:
    numbers = range(*file_range)
    N=[]
    for number in numbers:
        if number < 10:
            N.append(f"000{number}")
        elif 10 <= number < 100:
            N.append(f"00{number}")
        elif 100 <= number < 1000:
            N.append(f"0{number}")
        else:
            N.append(f"{number}")

    return N
