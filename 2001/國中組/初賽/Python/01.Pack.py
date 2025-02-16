while True:
    input_string = input()
    if input_string == "0":
        break
    num_stack = input_string.split()
    num = [int(number) for number in num_stack]
    if(num[0] < num[2] and num[1] < num[3]) or (num[1] < num[2] and num[0] < num[3]):
        print("yes")
    else:
        print("no")

exit()