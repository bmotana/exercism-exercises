"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_num = ["A", "B", "C", "D"]

    for x in range(number):
        yield seat_num[x % 4] 


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    
    seat_letter = ["A", "B", "C", "D"]

    letters = generate_seat_letters(4)

    counter = 0
    for s_n in range(1, number+1):
        if s_n == 13:
            continue
        for s_l in seat_letter:
            if counter == number:
                break
            yield str(s_n) + s_l
            counter += 1
        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    number_passenger = len(passengers)
    seats = generate_seats(number_passenger)
    seat_assignment = {}
    for person in passengers:
        seat_assignment[person] = next(seats)

    return seat_assignment


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_num in seat_numbers:
        zero_len = 12 - len(f'{seat_num}{flight_id}')
        yield f'{seat_num}{flight_id}{zero_len*"0"}'
