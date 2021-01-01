# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Name: Loganathan Bhavaneetharan
# Student ID: 20201212
# Date: 24/11/2020

print('''
WELCOME TO UOW, CREDIT PREDICTION PROGRAM!
+ - - - - - - - - - - - - - - - - - - - - - - +
|               PROGRAM MENU                  |
+ - - - - - - - - - - - - - - - - - - - - - - +           
|   1.STUDENT VERSION                         |              
|   2.STUDENT VERSION (VALIDATION)            |
|   3.STAFF VERSION WITH HISTOGRAM            |
|   4.STAFF VERSION WITH VERTICAL HISTOGRAM   |
|   5.ALTERNATIVE STAFF VERSION               |
|   6.EXIT                                    |
+ - - - - - - - - - - - - - - - - - - - - - - +
''')

bar = "-----------------------------------------------"

user_selection = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
count_list = []
total_count = 0

# Function for Credit Calculation
def calculation(pass_credit, defer_credit, fail_credit):

    global progress_count, trailer_count, retriever_count, exclude_count, count_list, total_count

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

        count_list = [progress_count, trailer_count, retriever_count, exclude_count]
        total_count = sum(count_list)

    else:
        print("Total incorrect")

    return progress_count, trailer_count, retriever_count, exclude_count, count_list, total_count


# Function for programs 3,4
def credit():
    
    global progress_count, trailer_count, retriever_count, exclude_count, count_list, total_count

    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0  

    while True:
        pass_credit = validate("pass  : ")
        defer_credit = validate("defer : ")
        fail_credit = validate("fail  : ")

        calculation(pass_credit, defer_credit, fail_credit)

        print("\nWould you like to enter another set of data? ")
        selection = input("Enter 'y' for yes or 'q' to quit and view results: ")
        selection = selection.lower()  # making user input lowercase
        print("")
        if selection == "q":
            break

    return progress_count, trailer_count, retriever_count, exclude_count


# Function for validation
def validate(credit_type):
    while True:
        try:
            user_input = int(input("Please enter your credits at " + credit_type))
        except ValueError:
            print("Integer Required")
            continue
        if user_input not in range(0, 121, 20):
            print("Out of Range")
            continue
        else:
            break

    return user_input


# Function for Calculating Stars
def stars(num):
    num_of_stars = num * "*"
    return num_of_stars


# Function for Printing Stars
def output(star_progress_count, star_trailer_count, star_retriever_count, star_exclude_count):
    print("Progress ", star_progress_count, " :", stars(star_progress_count))
    print("Trailer  ", star_trailer_count, " :", stars(star_trailer_count))
    print("Retriever", star_retriever_count, " :", stars(star_retriever_count))
    print("Excluded ", star_exclude_count, " :", stars(star_exclude_count))


while user_selection != 6:

    user_selection = int(input("PLEASE ENTER PROGRAM NUMBER: "))

    if user_selection == 1:
        print(bar)
        print("STUDENT VERSION")
        print(bar)
        pass_credit = int(input("Please enter your credits at pass_credit  : "))
        defer_credit = int(input("Please enter your credit at defer_credit  : "))
        fail_credit = int(input("Please enter your credit at fail_credit   : "))
        calculation(pass_credit, defer_credit, fail_credit)
        print(bar)

    elif user_selection == 2:
        print(bar)
        print("STUDENT VERSION (VALIDATION)")
        print(bar)
        pass_credit = validate("pass  : ")
        defer_credit = validate("defer : ")
        fail_credit = validate("fail  : ")
        calculation(pass_credit, defer_credit, fail_credit)
        print(bar)

    elif user_selection == 3:
        print(bar)
        print("STAFF VERSION WITH HISTOGRAM")
        print(bar)
        credit()
        print(bar)
        print("Horizontal Histogram")
        print(bar)
        output(progress_count, trailer_count, retriever_count, exclude_count)
        print("\n", total_count, "Outcomes in total.")
        print(bar)

    elif user_selection == 4:
        print(bar)
        print("STAFF VERSION WITH VERTICAL HISTOGRAM")
        print(bar)
        credit()
        print(bar)
        print("Vertical Histogram")
        print(bar)
        print("Progress", progress_count, "| Trailer", trailer_count, "| Retriever", retriever_count, "| Excluded", exclude_count)
        
        each_line = 0
        lines = max(count_list)
        length = len(count_list)

        while each_line < lines:
            columns = 0
            while columns < length:
                if each_line < int(count_list[columns]):
                    print('     *  ', end='     ')
                else:
                    print('        ', end='     ')
                columns += 1
            each_line += 1
            print("")

        print("\n", total_count, "Outcomes in total.")
        print(bar)

    elif user_selection == 5:
        print(bar)
        print("ALTERNATIVE STAFF VERSION")
        print(bar)

        progress_count = 0
        trailer_count = 0
        retriever_count = 0
        exclude_count = 0

        list_credit = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20], [40, 40, 40], [20, 40, 60],
                       [20, 20, 80], [20, 0, 100], [0, 0, 120]]

        for i in range(0, 10, 1):
            pass_credit = list_credit[i][0]
            defer_credit = list_credit[i][1]
            fail_credit = list_credit[i][2]
            calculation(pass_credit, defer_credit, fail_credit)

        print("")
        output(progress_count, trailer_count, retriever_count, exclude_count)
        print("\n", total_count, "Outcomes in total.")
        print(bar)

    elif user_selection == 6:
        print("PROGRAM ENDED!")
        break

    else:
        print("PLEASE ENTER A VALID NUMBER NEXT TIME!")
        break

print("\nTHANK YOU!")