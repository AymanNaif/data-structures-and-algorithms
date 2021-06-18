from asserts.ll_kth_from_end import *
import re
from typing import Counter


def zipLists(list1, list2):
    """
    take two linked lists and return one zip linked list
    """
    # regex= {[^}]+}
    elemnts_one = re.findall('{[^}]+}', str(list1))
    elemnts_two = re.findall('{[^}]+}', str(list2))
    strr = ''

    for i in range(len(elemnts_one)):

        strr += f'{elemnts_one[i]} -> {elemnts_two[i]} -> '
    strr += 'Null'
    return strr
