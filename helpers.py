# Sample: '1,2,5-7,10' -> [1,2,5,7,10]
def string_to_range(s):
    return sum(((list(range(*[int(j) + k for k,j in enumerate(i.split('-'))]))
         if '-' in i else [int(i)]) for i in s.split(',')), [])

# Sample [1,2,3] -> ['1','2','3'] 
def list_int_to_list_string(list_int):
    string_map = map(str, list_int)
    return list(string_map)

def ask_for_years_range(years):
    max_allowed = f'{min(years)}-{max(years)}'
    print(f"Range allowed: '{max_allowed}' or 'a' for all")
    str_range = input("Enter the year range: ")
    if str_range == 'a':
        str_range = max_allowed
    input_years = string_to_range(str_range)

    if min(input_years) < int(min(years)) and max(input_years) > int(max(years)):
        exit('Error: Invalid input.')

    return list_int_to_list_string(input_years)
