def uniq_add(my_list=[]):
    result = 0
    uniq_no = set(my_list)
    for value in uniq_no:
        result += value
    return(result)
