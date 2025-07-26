"""
@Author: Eden Tamari
"""

"""
        find_missing_item_v1: The function checks which number is missing in arithmetic sequence

        @Param:
                lst (list): the arithmetic sequence

        @Returns:
                 (int): the missing number
"""


def find_missing_item_v1(lst):
    if lst[0] < lst[1]:
        dic = min(lst[1] - lst[0], lst[2] - lst[1])
    else:
        dic = max(lst[1] - lst[0], lst[2] - lst[1])
    for i in range(0, len(lst) - 1):
        if lst[i] + dic != lst[i + 1]:
            return lst[i] + dic


"""
        find_missing_item_v2: The function checks which number is missing in arithmetic sequence

        @Param:
                lst (list): the arithmetic sequence

        @Returns:
                 (int): the missing number
"""


def find_missing_item_v2(lst):
    if lst[0] < lst[1]:
        dic = min(lst[1] - lst[0], lst[2] - lst[1])
    else:
        dic = max(lst[1] - lst[0], lst[2] - lst[1])
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if low + 1 == high:
            return lst[low] + dic
        if abs(lst[0] + mid * dic != lst[mid]):
            high = mid
        else:
            low = mid


"""
        split_list_index: The function finds an index in the list so that two
        consecutive foreign subgroups can be found in the list,
        one of which starts from position 0 up to the index
        position (inclusive) and the other from the next position
        after the index to the end so that their sum is the same.

        @Param:
                lst (list): list of integers
        @Returns:
                i (int): index splits the list
                or -1 if no such index exists
"""


def split_list_index(lst):
    sum_lst = sum(lst)
    sum_group = sum_lst / 2
    if not sum_group.is_integer():  # if it isnt int we wont find any index
        return -1
    for i in range(0, len(lst) - 1):  # i splits the list
        if sum(lst[:i + 1]) == sum(lst[i + 1:]):  # if left side == right side
            return i
    return -1


"""
        max_sequence: A recursive function that finds the sequence of
        numbers whose last digit is the same as the first
        digit of the next element in the list.

        @Param:
                lst (list): list of integers
                sequence (int): default sequence is 1
                seq_list (list): a list of sequences that the function found

        @Returns:
                 sequence (int): the max sequence of numbers whose last digit
                                is the same as the first digit of the next element
"""


def max_sequence(lst, sequence=1, seq_list=None):
    if seq_list == None:  # reset list
        seq_list = []
    if 1 == len(lst):  # stop conditions
        seq_list.append(sequence)
        return max(seq_list)
    if last_dig(lst[0]) == first_dig(lst[1]):
        max_sequence(lst[1:], sequence + 1, seq_list)  # seq ++
        return max(seq_list)
    elif last_dig(lst[0]) != first_dig(lst[1]):  # init seq and add to list
        seq_list.append(sequence)
        max_sequence(lst[1:], 1, seq_list)
        return max(seq_list)


"""
        first_dig: get first digit of number

        @Param:
                num (int): number
        @Returns:
                 (int): first digit
"""


def first_dig(num):
    str_num = str(num)
    return int(str_num[0])


"""
        last_dig: get last digit of number

        @Param:
                num (int): number
        @Returns:
                 (int): last digit
"""


def last_dig(num):
    str_num = str(num)
    return int(str_num[-1])


"""
        order: A recursive function that merges two strings into one string in ascending order

        @Param:
                s1 (str): A string of English lowercase letters
                s2 (str): A string of English lowercase letters

        @Returns:
                 merge_str (str): String merged and arranged in alphabetical order
"""


def order(s1, s2):
    if s1 == '' or s2 == '':
        return s1 + s2
    if s1[0] < s2[0]:
        return s1[0] + order(s1[1:], s2)
    else:
        return s2[0] + order(s1, s2[1:])
