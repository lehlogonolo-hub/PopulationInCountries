# Author: Aphane Jimmy
import random

from data import countries_and_capitals
from country import Country


def main():
    """
    The main function try’s to create a list of Country objects called all_countries
    (Assigning each one a random population between 1 million and 1 billion, in the try block)
    Using the countries_and_capitals tuple (use a loop)
    Make sure any ValueError exceptions are handled by printing “oops” to the console
    In addition to the ValueError’s message of “Population 1057988 is too low”.
    :return:
    """
    try:
        # Creating a list of Country objects
        all_countries = []
        for country, capital in countries_and_capitals:
            try:
                # Assigning each country a random population between 1 million and 1 billion
                population = random.randint(1000000, 1000000000)
                country_object = Country(country, capital, population)
                all_countries.append(country_object)
            except ValueError as e:
                print(f"Oops: {e}")

        # Loop through list and call print_details() for each object
        for country_objects in all_countries:
            country_objects.print_details()

        # Loop through list, call birth() for each object, and call print_details() again
        for country_objects in all_countries:
            country_objects.birth()
            country_objects.print_details()

        # Loop through list, call death() for each object, and call print_details() again
        for country_objects in all_countries:
            country_objects.death()
            country_objects.print_details()

        # Loop through list, call disaster() for each object, and call print_details() again
        for country_objects in all_countries:
            country_objects.disaster()
            country_objects.print_details()

    except ValueError as e:
        print(f"Oops: {e}")


if __name__ == "__main__":
    main()
