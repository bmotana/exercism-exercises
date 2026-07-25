import datetime    

def add(moment: datetime.datetime) -> datetime.datetime:
    """
    Adds one gigasecond (10^9 seconds) to the given datetime.

    Args:
    - moment (datetime.datetime): The initial datetime.

    Returns:
    - datetime.datetime: The datetime after adding one gigasecond.
    """
    # Define a timedelta representing one gigasecond (10^9 seconds)
    gigasecond = datetime.timedelta(seconds=10**9)
    
    # Add the gigasecond to the given moment and return the result
    return moment + gigasecond
