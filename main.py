"""Program takes user inputs to determine what average
grade is needed for the remainder of the class to
achieve a specified wanted mark in the chosen class"""

# Initialized variables for later use
average_grade = 0
final_weight = 0
first_weight = 0
valid_final_weight = True


# Function that adds evaluation marks and weights to corresponding arrays
def add_assignment():
    global final_weight
    global first_weight

    # Takes user input of the weight of their evaluation
    weight = input('Please enter evaluation weight ')
    # Takes user input for mark achieved in their evaluation
    mark = input('what was your grade on this evaluation? If none enter none ')

    # If mark entered is not none the value is added to an array of marks and the weight to an array of weights
    if mark != 'none':
        all_assignments_marks.append(float(mark))
        all_assignments_weights.append(float(weight))
        # Value of the weight is added to a variable for finished evaluations
        first_weight += float(weight)
    # If mark is none the weight is added to a separate array that contains weights of unfinished evaluations
    else:
        unfinished_weight.append(float(weight))
        # Value of the weight is added to a variable of unfinished evaluations
        final_weight += float(weight)


# Function calculates your current average grade
def average():
    global average_grade
    # Takes each value in arrays and uses them to calculate their average grade and add it to variable
    for x in range(len(all_assignments_marks)):
        average_grade += all_assignments_marks[x] * (all_assignments_weights[x]/100)

    return average_grade


# Function calculates average mark you need to achieve wanted mark
def average_needed():
    global final_weight
    global valid_final_weight
    mark_needed = (wanted_mark - average_grade)
    # If final weight is greater than 0 and less than 100 calculates mark needed
    if 0 < final_weight < 100:
        mark_needed /= final_weight
        mark_needed *= 100
    else:
        valid_final_weight = False

    return mark_needed


# Created array for marks
all_assignments_marks = []
# Created array for weights
all_assignments_weights = []
# Created array for unfinished weights
unfinished_weight = []

# Ask user for number of assignments
print('Please enter all evaluations for desired course, completed or uncompleted')
number_of_assignments = input('How many different evaluations are needed for the course? ')

# Loops for number of assignments and calls add assignment function each time
for assignment in range(int(number_of_assignments)):
    add_assignment()

    # Asks user what mark they want to achieve and calls average and average needed function
wanted_mark = int(input('What grade would you like to finish the course with? '))
average()
average_needed()

# Prints error message if incorrect input for weights earlier
if not valid_final_weight or average_needed() > 100:
    print('Incorrect amount of assignments added or grade not possible or all evaluations already complete')
# Prints average needed to achieve wanted mark
else:
    print('Average on remaining evaluations must be ' + str(average_needed()) + ' to achieve grade ' + str(
        wanted_mark))
