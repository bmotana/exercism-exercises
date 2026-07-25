"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False
        


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    
    """
    generated_power = voltage * current
    #  10 000 = 10 * 1000 green
    # 7000 = 10 * 700
    efficiency = int((generated_power/theoretical_max_power)*100)
    
    
    #  100% = (10 000/ 10 000) * 100 green
    #  70% = (70 000/ 10 000) * 100 orange

    if efficiency >= 80:
        return "green"
    elif efficiency < 80 and efficiency >= 60:
        return 'orange'
    elif efficiency < 60 and efficiency >= 30  :
        return 'red'
    elif efficiency < 30:
        return 'black'



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges

    
    """

    reactor_value = temperature * neutrons_produced_per_second

    lower_threshold = threshold * 0.9
    upper_threshold = threshold * 1.1

    if reactor_value < lower_threshold:
        return 'LOW'
    elif lower_threshold <= reactor_value <= upper_threshold:
        return 'NORMAL'
    else:
        return 'DANGER'

    # if reactor_value < threshold * 0.9 :
    #     # 10 * 399 = 3990 < 10 0000 * 0.9 =  9000 - low
    #     # 9001 < 9000
    #     # 4000 < 
    
    #     return "LOW"
    # elif reactor_value < threshold * 0.1 or reactor_value >= threshold * 0.1 :
        
    #     return "NORMAL"
    
    # elif  reactor_value < threshold * 0.1 :
    #     # 1000 * 30   30000 < 5000 * 0.1 = 500
    #     # 100
    #     return "DANGER"

