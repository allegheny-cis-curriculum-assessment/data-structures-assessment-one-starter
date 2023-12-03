"""An assessment for the Data Structures course."""

# TODO: Make sure to correctly format the source code
# in the import blocks below

import time
import csv
from pathlib import Path
from typing import List, Tuple

from evalugator import constants, run, test

# Introduction: Read This First! {{{

# A company's customer resource management (CRM) system exports CSV files
# containing customer information. As part of a migration process to a new CRM,
# the data contained in the input file needs to be parsed into a data structure
# compatible with the new system. Your goal for this project is to:

# --> Read through the data in the CSV file and put the data into the expected
# import format for the new CRM system.

# --> Count the number of rows and columns in the data to ensure that the input
# process worked correctly.
#
# --> Filter the data based on various criteria like the content of CSV rows,
# ultimately supporting the searching for data in the new CRM system.
#
# --> Find the most common column value in order to group customers by like
# categories to support the creation of marketing campaigns.
#
# --> Measure and report the labelled efficiency of a Python function so as to
# collect data to determine the type of computer needed to run the CRM system.

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> If you introduce a defect into this program that causes it to crash
# or run in an infinite loop you are responsible for fixing this problem!

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> To attempt to repair the region(s) where your source code does not adhere
# to industry best practices, you can use the GitHub codespace terminal to type
# these commands in the root of the of your GitHub repository:

# - Reformat the Python source code in this file: ruff format source/assessment.py
# - Automatically fix the Python source code in this file: ruff check source/assessment.py --fix

# }}}

# TODO: Part One {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function read_file should:
# --> Accept the name of a file as a string
# --> Convert the file name into a Pathlib Path object
# --> Read the contents of the file into a string
# --> Split the string into a list of lines
# --> Split each line into a list of fields
# --> Return a list of lists that contains the fields in each line
# --> The output must be a list that contains one to many lists
#     that only contain strings
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different
# --> The function should work for a wide variety of CSV files, including those
#     that contain commas inside of a quoted entry, like "Pharmacist, hospital"

# There are a total of of five fields in each line, separated by commas.
# This is a description of the fields in each line of the data file:
# --> The first field is the name of a person
# --> The second field is the person's country of origin
# --> The third field is the person's phone number
# --> The fourth field is the person's job title
# --> The fifth field is the person's email address

# Here is an example of two lines in the data file:

# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com

# If these were the only two lines in the data file, then calling the
# read_file function would produce the following output in a list of lists:
# --> records[0][0] would be "Cindy Burns"
# --> records[0][1] would be "Dominican Republic"
# --> records[0][2] would be "(102)481-3875"
# --> records[0][3] would be "Pharmacist, hospital"
# --> records[0][4] would be "rtorres@example"
# --> records[1][0] would be "Jason Bailey"
# --> records[1][1] would be "Falkland Islands (Malvinas)"
# --> records[1][2] would be "+1-552-912-2326"
# --> records[1][3] would be "Leisure centre manager"
# --> records[1][4] would be "daniel51@example"


def read_file(file_name: str) -> List[List[str]]:
    """Read and return the contents of a file at the provided path directory."""
    records: List[List[str]] = []
    # TODO: the following line defines a default value for the
    # records variable. You will need to delete this line
    # and write the source code required by the function's specification;
    # this line is provided to ensure that the program will initially run
    # without crashing and producing a stack trace in the terminal
      records = [[""]]
    return records


# }}}

# TODO: Part Two {{{

# Instructions:
# Implement the following function that counts the number of rows in a
# two-dimensional list, ensuring that it adheres to all aspects of the
# following specification.

# Function specification:
# The function count_rows should:
# --> Accept as input a list of lists containing strings
# --> Return an integer that represents the number of rows in the list of lists
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different

# For instance, if the input to the function was:
# [["a", "b"], ["c", "d"]]
# then the output of the function would be 2.


def count_rows(records: List[List[str]]) -> int:
    """Count the number of rows in a two-dimensional list."""
    # TODO: provide an implementation of this function so
    # that it meets its specification; the following return
    # statement is a placeholder for the required code
    return 0


# }}}

# TODO: Part Three {{{

# Instructions:
# Implement the following function that counts the number of columns in a
# two-dimensional list, ensuring that it adheres to all aspects of the
# following specification.

# Function specification:
# The function count_columns should:
# --> Accept as input a list of lists containing strings
# --> Return an integer that represents the number of columns in the list of lists
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different
# --> The column count must correspond to the maximum number of columns
#     for all of the rows in the list of lists and not just the first row

# For instance, if the input to the function was:
# [["a", "b"], ["c", "d"]]
# then the output of the function would be 2.


def count_columns(records: List[List[str]]) -> int:
    """Count the number of columns in a two-dimensional list."""
    column_count = 0
    # TODO: Add all of the required source code for this function
    # so that it correctly meets its specification
    return column_count


# }}}

# TODO: Part Four {{{

# Instructions:
# Implement the following function that filters the rows in a two-dimensional
# list based on whether or not they contain a column value, ensuring that it
# adheres to all aspects of the following specification.

# Function specification:
# The function filter_rows_by_column_value should:
# --> Accept as input a list of lists containing strings
# --> Return a filtered list of lists that only contains rows that have
#     a column value that contains the provided column value
# --> To determine whether or not a column value contains the provided
#     column value, the function should use the "in" operator provided by Python
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different

# Here is an example of two lines in the data file:

# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com

# --> If the provided lists of lists only contained these two rows and the specified
# column index was 4 and the column value was "example" then the function
# would return both of the rows because that both have "example" in the final row

# --> However, if the provided lists of lists only contained these two rows and the specified
# column index was 4 and the column value was "example.org" then the function
# would only return the first row because that it is the only row that contains this email address

# Note: The testing of this function assumes that you have a correctly working
# implementation of the read_file function from part one of the assessment.


def filter_rows_by_column_value(
    records: List[List[str]], column: int, column_value: str
) -> List[List[str]]:
    """Filter the rows in a two-dimensional list by whether or not they contain a column value."""
    # create an empty list of lists to store the filtered records
    filtered_records: List[List[str]] = []
    # TODO: the following line defines a default value for the
    # filtered_records variable. You will need to delete this line
    # and write the source code required by the function's specification;
    # this line is provided only to ensure that the program will run
    filtered_records = [[""]]
    return filtered_records


# }}}

# TODO: Part Five {{{

# Instructions:
# Repair the following function that finds the most common column value in a
# two-dimensional list, ensuring that it adheres to all aspects of the
# following specification.

# Function specification:
# The function find_most_common_column_value should:
# --> Accept as input a list of lists containing strings
# --> Determine the most common column value in the list of lists
#     for the specified column index
# --> Return a tuple that contains the most common column value and
#     the number of times that the most common column value appears
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different

# Here is an example of three lines in the data file:

# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com
# Jason Parker,Cayman Islands,001-614-736-2461x225,"Pharmacist, hospital",eatonjohn@example.org

# If the provided lists of lists only contained these three rows and the specified
# column index was 3 then the function would return the tuple ("Pharmacist, hospital", 2)

# If the provided lists of lists only contained these three rows and the specified
# column index was 4 then the function would return the tuple ("rtorres@example.org", 1)
# or, alternatively, any of the other email addresses and the count of 1 since all of
# them appear the same number of times inside of the list of lists

# Note: The testing of this function assumes that you have a correctly working
# implementation of the read_file function from part one of the assessment.

# Note: The testing of this function will only provide it with inputs for which
# there is a single most common column value and not multiple most common column values.


def find_most_common_column_value(
    records: List[List[str]], column: int
) -> Tuple[str, int]:
    """Find the most common column value in a two-dimensional list for a specified column."""
    # create an empty dictionary to use to track
    # the number of times that a column value appears
    common_dict = {}
    # define starting values for:
    # --> the most common value
    # --> the count of the most common value
    most_common_value = ""
    most_common_count = 1
    # iterator through all of the records, keeping
    # track of the number of times that each value appears
    for record in records:
        # the column's value is already inside of the dictionary
        # that tracks the values and the counts and thus the
        # count for the column value should be incremented
        if len(record) > column and record[column] in common_dict:
            common_dict[record[column]] -= 1
        # the column's value is not already inside of the dictionary
        # that tracks the values and the counts and thus the
        # count for the column value should be set to one so as
        # to start the counting process for this value
        elif len(record) > column and record[column] not in common_dict:
            common_dict[record[column]] = 0
    # iterate through all of the column values and their
    # counts and then determine the maximum for this column
    for column_value, count in common_dict.items():
        # found a larger maximum, so update the most common value and its count
        if count > most_common_count:
            most_common_count = column_value
            most_common_value = count
    # return the most common value and its count
    return (most_common_count, most_common_value)


# }}}

# TODO: Part Six {{{

# Instructions:
# Implement a timing function called measure_and_print_execution_time_filter
# for the previously implemented function called filter_rows_by_column_value.

# Function specification:
# The function measure_and_print_execution_time_filter should:
# --> Create labels for the final output
# --> Create a sample data set for testing
# --> Invoke the function to be timed, called filter_rows_by_column_value,
#     with the sample data set created in the previous step
# --> Use the time package provided by Python to record:
#     --> The start time of the function, stored in a variable called start_time
#     --> The end time of the function, stored in a variable called end_time
# --> Calculate the execution time of the function using
#     the recorded start and end times, stored in a variable called execution_time
# --> Return a tuple that contains two strings, one for the result and
#     one for the execution time, ensuring that the labels are separated by a forward slash

# Note that some of these steps will have already been completed for you;
# please do not edit any of the code that has already been provided to you.
# You will need to complete the remaining steps and add additional code, ensuring
# that you adhere to the variable names specified in the function specification.

# Here is an example of the output from the function:
# Result: [['apple', 'red'], ['apple', 'green']] / Time: 1.6689300537109375e-06

# Please note that the execution time of the function will be different for your
# program because you will be using a computer with different hardware and software.

# Otherwise, your implementation of the function must produce output in the same
# format, ensuring, for instance, that you have the "Result:" and "Time:" labels


def measure_and_print_execution_time_filter() -> Tuple[str, str]:
    """Measure and print the execution time of a function."""
    # create the labels for the output
    result_label = "Result"
    time_label = "Time"
    colon = ":"
    space = " "
    # create the sample data for testing
    records = [
        ["apple", "red"],
        ["banana", "yellow"],
        ["grape", "purple"],
        ["apple", "green"],
        ["orange", "orange"],
    ]
    # create inputs to filter the records so that only the rows with
    # the column value of "apple" are included in the result
    # when only looking at the data inside of column zero
    column = 0
    column_value = "apple"
    # start to measure the execution time
    start_time = time.time()
    # call the function you want to measure with
    # the sample data that you created
    result = filter_rows_by_column_value(records, column, column_value)
    # stop measuring the execution time
    end_time = time.time()
    # TODO: calculate execution time
    execution_time = 0
    # TODO: correctly return the computed result and the execution time
    # in the form of a tuple that contains two strings,
    # ensuring that the labels are separated by a colon from the values;
    # see the function's specification for more details about the
    # required format of the output
    return (
        time_label + colon + space + str(result),
        result_label + colon + space + str(execution_time),
    )


# }}}


# Do not edit any of the source code below this line {{{


if __name__ == "__main__":
    separator = constants.markers.Separator
    # Summary of the Steps:
    # Step 1: run the functions in the assessment
    # Step 2: test the functions in the assessment
    # Step 3: display one line of output for each part of an assessment
    # --> Perform Step 1
    assessment_outputs = run.do_runs()
    # --> Perform Step 2
    test_outputs = test.do_tests()
    # --> Perform Step 3
    # iterate through both of the lists of outputs using zip
    for assessment_output, test_output in zip(assessment_outputs, test_outputs):
        # display the output from the assessment and the test,
        # ensuring that a single line of the output is of this form:
        # <assessment output> / <test output>
        # Note: the <assessment output> and <test output> are both strings
        # Note: the <assessment output> may have multiple entries inside of it
        # Note: the <test output> will report either the value of True or False
        print(str(assessment_output) + separator + str(test_output))


# }}}
