# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Name: Loganathan Bhavaneetharan
# Student ID: 20201212
# Date: 24/11/2020

bar = "-----------------------------------------------"

# Declaring integer variables to count the outputs of results
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

# We are using a two dimensional list to store the data
list_credit = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20], [40, 40, 40], [20, 40, 60],
               [20, 20, 80], [20, 0, 100], [0, 0, 120]]

# We are using a for loop to iterate through the list
for i in range(0, 10, 1):
    pass_credit = list_credit[i][0]
    defer_credit = list_credit[i][1]
    fail_credit = list_credit[i][2]

    # Comparing inputs using conditional statements
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


# Using an user defined function called stars to print out the certain number of stars
def stars(num):
    num_of_stars = num * "*"
    return num_of_stars


# Getting total outcomes
total_count = progress_count + trailer_count + retriever_count + exclude_count

print(bar)
print("Progress ", progress_count, " :", stars(progress_count))
print("Trailer  ", trailer_count, " :", stars(trailer_count))
print("Retriever", retriever_count, " :", stars(retriever_count))
print("Excluded ", exclude_count, " :", stars(exclude_count))
print(bar)
print(total_count, "Outcomes in total.")
