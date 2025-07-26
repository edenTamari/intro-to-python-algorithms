from intro_to_python_algorithms import (find_missing_item_v1,
                                        find_missing_item_v2,
                                        split_list_index,
                                        max_sequence, order)


def main():
    lst1 = [5, 7, 11, 13, 15]
    lst2 = [3, 9, 12, 15, 18]
    lst3 = [6, 2, -2, -6, -14]
    lst4 = [1, 2, 3, 4, 6]

    print("***********Q1A**************")
    print(find_missing_item_v1(lst1))  # 9
    print(find_missing_item_v1(lst2))  # 6
    print(find_missing_item_v1(lst3))  # -10
    print(find_missing_item_v1(lst4))  # 5
    print("***********Q1B**************")
    print(find_missing_item_v2(lst1))  # 9
    print(find_missing_item_v2(lst2))  # 6
    print(find_missing_item_v2(lst3))  # -10
    print(find_missing_item_v2(lst4))  # 5

    lst5 = [1, 3, -1, 2, -2, 7]
    lst6 = [1, -2, 7, 0, 3]
    lst7 = [2, 3, 4, 8, 1]

    print("***********Q2**************")
    print(split_list_index(lst5))  # 3
    print(split_list_index(lst6))  # -1
    print(split_list_index(lst7))  # 2

    lst8 = [15, 52, 25, 1981, 123, 33, 321]
    lst9 = [9, 196, 606, 1981]
    lst10 = [1234]

    print("***********Q3**************")
    print(max_sequence(lst8))  # 4
    print(max_sequence(lst9))  # 2
    print(max_sequence(lst10))  # 1

    s1 = 'acct'
    s2 = 'bbdz'
    s3 = 'a'
    s4 = 'a'
    s5 = 'cd'
    s6 = 'ab'
    s7 = ''
    s8 = 'ab'

    print("***********Q4**************")
    print(order(s1, s2))  # 'abbcctz'
    print(order(s3, s4))  # 'aa'
    print(order(s5, s6))  # 'abcd'
    print(order(s7, s8))  # 'ab'


if __name__ == "__main__":
    main()
