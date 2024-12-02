def pair_and_filter(list1, list2, filter_function = None):
    result = []
    a = tuple()
    for x in list1:
        for y in list2:
            if filter_function == None:
                a += (x, y)
                result.append(a)
                a = tuple()
            else:
                if filter_function(x,y):
                    a += (x,y)
                    result.append(a)
                    a = tuple()
    return result




print(pair_and_filter([1, 2], [3, 4], filter_function=lambda x, y: (x + y) % 2 == 0))

def concat_or_upper(strings, uppercase = None):
    if uppercase:
        return (" ".join(strings)).upper()
    else:
        return " ".join(strings)

print(concat_or_upper(["Hello", "World!", "awdad"], True))



def filter_uppercase_strings(arg):
    result = []
    for i_1 in arg:
        if i_1 == i_1.upper():
            result.append(i_1)
    return result


print(filter_uppercase_strings(['FFF','Fd','cds', "232F"]))


def unique_sorted_elements(*arg):
    combined_list = []
    for i in arg:
        combined_list.extend(i)
    result = sorted(set(combined_list))
    return result


print(unique_sorted_elements(["1","2"], ["2","3"], ["3", "4"]))