#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            results = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            results = 0
            print("wrong type")
        except ZeroDivisionError:
            results = 0
            print("division by 0")
        except IndexError:
            results = 0
            print("out of range")
        finally:
            new_list.append(results)
    return new_list
