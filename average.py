def is_number(num):
    typ = type(num)
    return typ == int or typ == float

def average(list_of_numbers):

    # validate the list
    for num in list_of_numbers:
        if not is_number(num):
            return "numbers only"

    return sum(list_of_numbers)/ len(list_of_numbers)

if __name__ == "__main__":
    array_of_nums = [3, 4, 63, 4]
    average_of_array_of_nums = average(array_of_nums)
    print("The average of list {} is {}".format(array_of_nums, average_of_array_of_nums))