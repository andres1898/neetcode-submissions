def add_two_numbers() -> int:
    user_input = input()
    list_number = user_input.split(",")
    result_number = int(list_number[0]) + int(list_number[1])
    return result_number




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
