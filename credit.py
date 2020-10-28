from math import floor

cc_num = input("Number: ")

sum = 0
i = -1
cc_num_len = len(cc_num)

while i >= -cc_num_len:
    if i % 2 == 1:
        sum += int(cc_num[i])
    else:
        double_curr_digit = int(cc_num[i]) * 2
        while(double_curr_digit > 0):
            sum += double_curr_digit % 10
            double_curr_digit = floor(double_curr_digit / 10)
    i -= 1

if sum % 10 == 0:
    if (cc_num_len == 15) and (cc_num[0] == "3") and (cc_num[1] == "4" or cc_num[1] == "7"):
        print("AMEX")
    elif cc_num_len == 16 and cc_num[0] == "4":
        print("VISA")
    elif (cc_num_len == 13 or cc_num_len == 16) and (cc_num[0] == "5") and (cc_num[1] == "1" or cc_num[1] == "2" or cc_num[1] == "3" or cc_num[1] == "4" or cc_num[1] == "5"):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")
