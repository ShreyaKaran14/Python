def even(list):
    for num in list:
        if(num % 2) == 0:
            print(num, end=" ")
list = [10, 21, 4, 45, 66, 93]
even(list)