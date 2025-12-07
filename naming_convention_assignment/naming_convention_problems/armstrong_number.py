def compute_armstrong_sum(user_input_number):
    # Initializing Sum and Number of Digits
    armstrong_sum = 0
    digit_count = 0

    # Calculating Number of individual digits
    remaining_number = user_input_number 
    while remaining_number > 0:
        digit_count = digit_count + 1 
        remaining_number = remaining_number // 10 

    # Finding Armstrong Number
    remaining_number = user_input_number 
    for iteration_index in range(1, remaining_number + 1): 
        last_digit = remaining_number % 10 
        armstrong_sum = armstrong_sum + (last_digit ** digit_count) 
        remaining_number //= 10 
    return armstrong_sum

user_input_number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

if (user_input_number == compute_armstrong_sum(user_input_number)):
    print("\n %d is Armstrong Number.\n" % user_input_number)
else:
    print("\n %d is Not a Armstrong Number.\n" % user_input_number)