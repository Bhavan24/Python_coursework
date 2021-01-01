
bar = "-----------------------------------------------"

print(bar)
print("Staff Version with Histogram\n")
# Declaring variable user_selection for user selection ("y" or "q")
user_selection = "y"

# Declaring integer variables to count outputs of results
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

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

# Using the while loop until user quits the program
while user_selection == "y":

    # calling function "validate" and setting the user inputs
    pass_credit = validate("pass  : ")
    defer_credit = validate("defer : ")
    fail_credit = validate("fail  : ")


    print(bar)
    # Comparing user inputs using conditional statements
    if pass_credit + defer_credit + fail_credit == 120:
        if (pass_credit == 120) and (defer_credit == 0) and (fail_credit == 0):
            print("Progress")
            progress_count += 1
        elif (pass_credit == 100) and (0 <= defer_credit <= 20) and (0 <= fail_credit <= 20):
            print("Progress (module trailer)")
            trailer_count += 1
        elif (0 <= pass_credit <= 40) and (0 <= defer_credit <= 40) and (80 <= fail_credit <= 120):
            print("Exclude")
            exclude_count += 1
        else:
            print("Do not progress – module retriever")
            retriever_count += 1
    else:
        print("Total incorrect")

    print(bar)
    print("\nWould you like to enter another set of data? ")
    user_selection = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print("")
    # Making the user input lower case, so even if the user enters a uppercase letter program works perfectly
    user_selection = user_selection.lower()
    # if user enters "q" we are breaking out of the loop
    if user_selection == "q":
        break


# Using an user defined function called stars to print out the certain number of stars
def stars(num):
    num_of_stars = num * "*"
    return num_of_stars


# Getting total outcomes
total_count = progress_count + trailer_count + retriever_count + exclude_count

print(bar)

print("Horizontal Histogram")
print("Progress ", progress_count, " :", stars(progress_count))
print("Trailer  ", trailer_count, " :", stars(trailer_count))
print("Retriever", retriever_count, " :", stars(retriever_count))
print("Excluded ", exclude_count, " :", stars(exclude_count))

print("\n", total_count, "Outcomes in total.")
print(bar)
