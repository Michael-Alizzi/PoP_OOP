"""Name: Michael Alizzi
Student Id: 5651718
Temperature Module"""

# Fahrenheit = (9/5 x Celsius) + 32
def celsius_to_fahren(celsius):
    """Converts Celsius (C) to Fahrenheit (F)."""
    return (9/5 * celsius) + 32


# Kelvin = Celsius + 273.15
def celsius_to_kelvin(celsius):
    """Converts Celsius (C) to Kelvin (K)."""
    return celsius + 273.15


# Celsius = (Fahrenheit - 32) × 5/9
def fahren_to_celsius(fahren):
    """Converts Fahrenheit (F) to Celsius (C)."""
    return (fahren - 32) * 5/9


### Formula for converting Fahrenheit (F) to Kelvin (K) ###

# Celsius = Kelvin - 273.15
# Celsius = (Fahrenheit - 32) × 5/9
# Kelvin - 273.15 = (Fahrenheit - 32) × 5/9

# Kelvin = (5/9) x (Fahrenheit - 32) + 273.15
def fahren_to_kelvin(fahren):
    """Converts Fahrenheit (F) to Kelvin (K)."""
    return (5/9) * (fahren - 32) + 273.15


# Celsius = Kelvin - 273.15
def kelvin_to_celsius(kelvin):
    """Converts Kelvin (K) to Celsius (C)."""
    return kelvin - 273.15


### Formula for converting Kelvin (K) to Fahrenheit (F) ###

# Inverse: Kelvin = (5/9) x (Fahrenheit - 32) + 273.15

# Fahrenheit = (9/5) * (K - 273.15) + 32
def kelvin_to_fahren(kelvin):
    """Converts Kelvin (K) to Fahrenheit (F)."""
    return (9/5) * (kelvin - 273.15) + 32


class Temperature:
    """A class to store and transform temperatures."""
    def __init__(self, n, u):
        """Creating temperature and scale attributes."""
        # Create the temperature attribute
        self.temperature = n

        # Create the unit attribute
        try:
            if u.upper() in ['C', 'F', 'K']:
                self.unit = u.upper()
            else:
                print(
                    "Wrong letter. Choose either Celsius ('C'), "
                    "Fahrenheit ('F'), or Kelvin ('K')!"
                )

        except AttributeError:
            print(
                "No letter provided. Please choose either Celsius ('C'), "
                "Fahrenheit ('F'), or Kelvin ('K')!"
                )

    # Print information about an instance of the Temperature class
    def __str__(self):
        try:
            return f"Temperature: {self.temperature} {self.unit}"
        except AttributeError:
            return (
                "You haven't created the instance of the Temperature "
                "class correctly!"
            )

    def to(self, unit, decimal = None):
        """Method to convert 'temperature a' to 'temperature b'."""
        try:
            # Converts to Celsius from Fahrenheit or Kelvin
            if unit.upper() == 'C':
                converted_unit = fahren_to_celsius(
                    self.temperature
                    ) if self.unit == 'F' else kelvin_to_celsius(
                        self.temperature
                        )
            # Converts to Fahrenheit from Celsius or Kelvin
            elif unit.upper() == 'F':
                converted_unit = celsius_to_fahren(
                    self.temperature
                    ) if self.unit == 'C' else kelvin_to_fahren(
                        self.temperature
                        )
            # Converts to Kelvin from Celsius or Fahrenheit
            elif unit.upper() == 'K':
                converted_unit = fahren_to_kelvin(
                    self.temperature
                    ) if self.unit == 'F' else celsius_to_kelvin(
                        self.temperature
                        )
            else:
                return (
                "Choose a temperature to convert to, either "
                "Celsius ('C'), Fahrenheit ('F'), or Kelvin ('K')!"
                )

            # Round final value if required
            if decimal is None:
                return converted_unit
            else:
                return round(converted_unit, decimal)

        except AttributeError:
            return ("The instance of the Temperature class hasn't been "
                   "correctly or\nthe to() method has not received a letter."
                   )
        except TypeError:
            return "The to() method hasn't received an integer to round to!"

    # Defining comparison between two instances
    def __eq__(self, other):
        return self.temperature == other.temperature

    def __ne__(self, other):
        return self.temperature != other.temperature

    def __lt__(self, other):
        return self.temperature < other.temperature

    def __le__(self, other):
        return self.temperature <= other.temperature

    def __gt__(self, other):
        return self.temperature > other.temperature

    def __ge__(self, other):
        return self.temperature >= other.temperature
    