#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40
# def EXPECTED_BAKE_TIME():
#     return 40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_bake_time = EXPECTED_BAKE_TIME - time
    return elapsed_bake_time
    
#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

def preparation_time_in_minutes(number_of_layers):

    """
    Calculate the prepartion time for each layer of lasagne

    :param number_of_layers (int): the number of layers of lasagne
    :returns: the total time it takes to prepares each layer of lasagne

    this function takes the number of layers you would add to the lasagne multiples them by the time it would to do each layer\
    and gives you the prepartion time in minutes
    """
    PREPARATION_TIME = number_of_layers * 2
    return PREPARATION_TIME 
    
#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :param number_of_layers: number of layers
    :return: total time it takes to to cook 

    Function that takes number of layer and the elapsed bake time and returns the total number of time cooking
    """

    total = number_of_layers * 2 + elapsed_bake_time
    return total
