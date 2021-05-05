# Sample: '1,2,5-7,10' -> [1,2,5,7,10]
def string_to_range(s):
    return sum(((list(range(*[int(j) + k for k,j in enumerate(i.split('-'))]))
         if '-' in i else [int(i)]) for i in s.split(',')), [])

# Sample [1,2,3] -> ['1','2','3'] 
def list_int_to_list_string(list_int):
    string_map = map(str, list_int)
    return list(string_map)

def ask_for_option():
    print("1. Generate table")
    print("2. Generate plots")
    option = int(input("Which option 1 or 2:"))

    if option not in [1,2]:
        exit('Error: Invalid option.')

    return option

def ask_for_years_range(years):
    max_allowed = f'{min(years)}-{max(years)}'
    print(f"Range allowed: '{max_allowed}' or 'a' for all")
    str_range = input("Enter the year range: ")
    if str_range == 'a':
        return years
    input_years = string_to_range(str_range)

    if min(input_years) < int(min(years)) and max(input_years) > int(max(years)):
        exit('Error: Invalid input.')

    return list_int_to_list_string(input_years)

def normalize(values, lower, upper):
    max_value = max(values)
    min_value = min(values)
    if(max_value == min_value):
        return upper + lower / 2
    return [lower + (x - min_value) * (upper - lower) / (max_value - min_value) for x in values]