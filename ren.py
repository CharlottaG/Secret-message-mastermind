
user_input = 1234
random_code = 1354

user_input_array = [int(x) for x in str(user_input)]
random_code_array = [int(x) for x in str(random_code)]

def check_num_position(user_input_array, random_code_array):

    for x, y in zip(user_input_array, random_code_array):
        if x == y:
            print("Right")
        else:
            print("Wrong")

check_num_position(user_input_array, random_code_array)