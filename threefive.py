def print_numbers() -> None:
    """
    A program that prints the numbers from 1 to 100. 
    But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. 
    For numbers which are multiples of both three and five print “ThreeFive”.
    """

    multiples: dict = {3:"Three", 5:"Five"}

    for number in range(1, 101):
        string_output: str = "".join(
            value for key, value in multiples.items() if number % key == 0
        )    
        print(string_output or number)

print_numbers()
