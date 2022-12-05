#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list.copy()
    if idx < 0 or idx >= len(a):
        return(my_list)
    a[i] = element
    return(a)
