# Aphane Jimmy

class Country:
    def __init__(self, country_name, capital_name, population):
        if population < 2000000:
            raise ValueError(f"Population {population} is too low")

        self.country_name = country_name
        self.capital_name = capital_name
        self.population = population

    def print_details(self):
        """Prints the details about Country and their Capitals"""
        print(f"The capital of {self.country_name} (pop. {self.population}) is {self.capital_name.upper()}")

    def birth(self):
        """Adds 1 to the object’s own self’s population"""
        self.population += 1

    def death(self):
        """"Subtracts 1 from the object’s own self’s population"""
        self.population -= 1

    def disaster(self):
        """
        For countries with a population of 100 million or higher,
        Subtracts 100 million from the population.
        For smaller countries, it sets the population to 0
        """
        if self.population >= 100000000:
            self.population -= 100000000
        else:
            self.population = 0