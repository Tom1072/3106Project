
def dict_list_to_tuple_list(dict_list: list):
    output = []
    for i in range(len(dict_list)):
        output.append(dict_list[i].items())

    output.sort()
    return output
