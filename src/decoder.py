#!/usr/bin/env python3

from linked_list import LinkedList
from cipher import FileDecoder, DecryptException
from os import path

import string
import re
import calendar

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " \n"


def main():
    # Get required input from user, if file opened successfully, create FileDecoder object with file info.
    file_decoder = get_input()

    list_of_months = LinkedList()  # Create an empty linked list to store month info.

    for row in file_decoder:  # Iterate through the decoded file rows.
        dictionary = to_dict(file_decoder.header_line, row)  # Store info into dictionary.

        # Get the time delay of the current ferry
        time_diff = get_time_diff(dictionary['scheduled_departure_hour'],
                                  dictionary['scheduled_departure_minute'],
                                  dictionary['actual_departure_hour'],
                                  dictionary['actual_departure_minute'])

        # Get the name of the month that the current ferry operated in
        month = get_month_name(int(dictionary['scheduled_departure_month']))

        # Insert current ferry info into linked list.
        list_of_months.insert(month, time_diff)

    print_output(list_of_months, file_decoder)  # Print the average ferry time delay for each month.


def get_input():
    """ Gets filename and password, decodes file, returns FileDecoder object """

    file_name = get_file_name()

    while True:
        password = get_key()
        try:
            return FileDecoder(password, file_name, alphabet)
        except DecryptException:
            print("Failed to decrypt file, please try again")
            continue


def get_file_name():
    """ Gets filename, if invalid, keep asking for it """

    file_name = input("Enter name of file: ")

    if file_name.casefold() == 'q':
        print("exiting...", end='')
        exit()

    if path.exists(file_name):
        return file_name

    print("File not found. Try again. Type 'q' to exit.")
    return get_file_name()


def get_key():
    """ Gets password, if invalid format or if can't decode file, keep asking for it """

    key = input("Enter password: ")

    if key.casefold() == 'q':
        print("exiting...", end='')
        exit()

    if check_key_validity(key):
        return key

    print("The password format is not valid. Type 'q' to exit.")
    return get_key()


def check_key_validity(key):
    """ Checks if password is of valid format, true if it is, false if not """

    return bool(re.search(r'[A-Z]', key)) and \
        bool(re.search(r'\d+.*\d+', key)) and \
        bool(re.match(r'^[^!@#$&*\-_.]*[!@#$&*\-_.][^!@#$&*\-_.]*[!@#$&*\-_.][^!@#$&*\-_.]*$', key)) and \
        bool(re.match(r'^.{6,8}$', key))


def to_dict(header_line, line):
    """ Convert a csv header line and information into dictionary """
    """ (with header line as keys and information as values) """

    return dict(zip(header_line, line))


def get_time_diff(scheduled_hour, scheduled_min, actual_hour, actual_min):
    """ Gets the time delay of a certain ferry """

    tot_scheduled_min = convert_to_min(float(scheduled_hour)) + float(scheduled_min)
    tot_actual_min = convert_to_min(float(actual_hour)) + float(actual_min)

    return tot_actual_min - tot_scheduled_min


def convert_to_min(time):
    """ Converts hours to minutes """

    return time * 60


def get_month_name(mon):
    """ Given a month number, returns the first 3 letters of the month name """

    return calendar.month_name[mon][:3]


def print_output(list_of_months, file_decoder):
    """ Prints output with format """
    print()
    print("RESULTS")
    print("FileDecoder: " + str(file_decoder))
    print("Entries: " + str(len(file_decoder)))
    curr = list_of_months.head
    while curr is not None:
        print("    Average delay for %s: %.2f" % (curr.month, get_avg(curr.time_diff)))
        curr = curr.next

    print("END")


def get_avg(lis):
    """ Computes the average of a list """

    return sum(lis) / len(lis)


if __name__ == '__main__':
    main()
