# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Name: Loganathan Bhavaneetharan
# Student ID: 20201212
# Date: 24/11/2020

bar = "-----------------------------------------------"

print(bar)

pass_credit = int(input("Please enter your credits at pass  : "))
defer_credit = int(input("Please enter your credit at defer  : "))
fail_credit = int(input("Please enter your credit at fail   : "))

print(bar)

# Comparing user inputs using conditional statements
if (pass_credit == 120) and (defer_credit == 0) and (fail_credit == 0):
    print("Progress")
elif (pass_credit == 100) and (0 <= defer_credit <= 20) and (0 <= fail_credit <= 20):
    print("Progress (module trailer)")
elif (0 <= pass_credit <= 40) and (0 <= defer_credit <= 40) and (80 <= fail_credit <= 120):
    print("Exclude")
else:
    print("Do not progress – module retriever")

print(bar)
