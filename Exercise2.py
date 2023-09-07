# takes two input
def get_dict(dict1, dict2):
    combined_dict = {}
    
# takes both keys that are common
    for key in dict1.keys() & dict2.keys():
        combined_dict[key] = dict1[key] + dict2[key]
        
# retur combinatoin
    return combined_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_dict(my_dict_1, my_dict_2)
print(combined_dict)
