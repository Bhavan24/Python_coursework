# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Name: Loganathan Bhavaneetharan
# Student ID: 20201212
# Date: 24/11/2020

bar = "-----------------------------------------------"
print(bar)

# Using an user defined function called validate for error handling part
def validate(credit_type):
    # Performing a loop until user enters the correct input
    while True:
        # checking input is an integer or not
        try:
            user_input = int(input("Please enter your credits at " + credit_type))
        except ValueError:
            print("Integer Required")
            continue
        # checking the range 0, 20, 40, 60, 80, 100, 120 using range function
        if user_input not in range(0, 121, 20):
            print("Out of Range")
            continue
        else:
            break

    return user_input


# calling validate function and setting user inputs
pass_credit = validate("pass  : ")
defer_credit = validate("defer : ")
fail_credit = validate("fail  : ")

print(bar)

# Comparing user inputs using conditional statements
if pass_credit + defer_credit + fail_credit == 120:
    if (pass_credit == 120) and (defer_credit == 0) and (fail_credit == 0):
        print("Progress")
    elif (pass_credit == 100) and (0 <= defer_credit <= 20) and (0 <= fail_credit <= 20):
        print("Progress (module trailer)")
    elif (0 <= pass_credit <= 40) and (0 <= defer_credit <= 40) and (80 <= fail_credit <= 120):
        print("Exclude")
    else:
        print("Do not progress – module retriever")
else:
    print("Total incorrect")

print(bar)
