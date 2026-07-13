from typing import List

def read_integers() -> List[int]:
    user_input = input()
    list_string = user_input.split(",")
    list_int = []

    for number in list_string:
        as_int = int(number)
        list_int.append(as_int)

    return(list_int) 

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
