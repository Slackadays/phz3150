import sys
import numpy as np

def triathalon_time(sports, athletes):
    """Prints which participant will finish first and their expected time in hours, and which one will finish last and their expected time in hours given an input of arrays of sports and athletes."""

    id_to_participant = {"1": "Mary", "2": "John", "3": "Peter", "4": "Mafalda", "5": "Paul", "6": "Lionel"}

    fastest_swimmer_index = 0
    fastest_swimming_speed = 0
    for i in range(len(athletes)):
        if athletes[i][1] > fastest_swimming_speed:
            fastest_swimming_speed = athletes[i][1]
            fastest_swimmer_index = i

    slowest_swimmer_index = 0
    slowest_swimming_speed = sys.maxsize
    for i in range(len(athletes)):
        if athletes[i][1] < slowest_swimming_speed:
            slowest_swimming_speed = athletes[i][1]
            slowest_swimmer_index = i

    print( 'For swimming which has an average distance of ' + str(sports[0]) + ', ' + id_to_participant[str(fastest_swimmer_index + 1)] + ' is expected to finish first with a time of ' + str(sports[0] / athletes[fastest_swimmer_index][1] / 60 / 60) + ' hours, and ' + id_to_participant[str(slowest_swimmer_index + 1)] + ' is expected to finish last with a time of ' + str(sports[0] / athletes[slowest_swimmer_index][1] / 60 / 60) + ' hours.')

    fastest_biker_index = 0
    fastest_biking_speed = 0
    for i in range(len(athletes)):
        if athletes[i][2] > fastest_biking_speed:
            fastest_biking_speed = athletes[i][2]
            fastest_biker_index = i

    slowest_biker_index = 0
    slowest_biking_speed = sys.maxsize
    for i in range(len(athletes)):
        if athletes[i][2] < slowest_biking_speed:
            slowest_biking_speed = athletes[i][2]
            slowest_biker_index = i

    print( 'For biking which has an average distance of ' + str(sports[1]) + ', ' + id_to_participant[str(fastest_biker_index + 1)] + ' is expected to finish first with a time of ' + str(sports[1] / athletes[fastest_biker_index][2] / 60 / 60) + ' hours, and ' + id_to_participant[str(slowest_biker_index + 1)] + ' is expected to finish last with a time of ' + str(sports[1] / athletes[slowest_biker_index][2] / 60 / 60) + ' hours.')

    fastest_runner_index = 0
    fastest_running_speed = 0
    for i in range(len(athletes)):
        if athletes[i][3] > fastest_running_speed:
            fastest_running_speed = athletes[i][3]
            fastest_runner_index = i

    slowest_runner_index = 0
    slowest_running_speed = sys.maxsize
    for i in range(len(athletes)):
        if athletes[i][3] < slowest_running_speed:
            slowest_running_speed = athletes[i][3]
            slowest_runner_index = i

    print( 'For running which has an average distance of ' + str(sports[2]) + ', ' + id_to_participant[str(fastest_runner_index + 1)] + ' is expected to finish first with a time of ' + str(sports[2] / athletes[fastest_runner_index][3] / 60 / 60) + ' hours, and ' + id_to_participant[str(slowest_runner_index + 1)] + ' is expected to finish last with a time of ' + str(sports[2] / athletes[slowest_runner_index][3] / 60 / 60) + ' hours.')

    # I copied and pasted a lot of code here :)

def triathalon_time_dict(sports: dict, athletes_times: dict):
    """Prints which participant will finish first and their expected time in hours, and which one will finish last and their expected time in hours given an input of dictionaries of sports and athletes."""

    def fastest_and_slowest(sport, sport_index):
        fastest_athlete = ''
        fastest_time = sys.maxsize
        for athlete in athletes_times:
            if sports[sport] / athletes_times[athlete][sport_index] / 60 / 60 < fastest_time:
                fastest_time = sports[sport] / athletes_times[athlete][sport_index] / 60 / 60
                fastest_athlete = athlete

        slowest_athlete = ''
        slowest_time = 0
        for athlete in athletes_times:
            if sports[sport] / athletes_times[athlete][sport_index] / 60 / 60 > slowest_time:
                slowest_time = sports[sport] / athletes_times[athlete][sport_index] / 60 / 60
                slowest_athlete = athlete

        print( 'For ' + sport + ' which has an average distance of ' + str(sports[sport]) + ', ' + fastest_athlete + ' is expected to finish first with a time of ' + str(fastest_time) + ' hours, and ' + slowest_athlete + ' is expected to finish last with a time of ' + str(slowest_time) + ' hours.')

    fastest_and_slowest("swimming", 0)

    fastest_and_slowest("biking", 1)

    fastest_and_slowest("running", 2)

def my_circuit(circuit_type: str, resistors: int, resistances: list, v_or_a: float):
    """Prints information about the total resistance and voltage/amperage of a circuit given whether it's series or parallel, how many resistors there are, what reisstances they have, and the voltage/amperage of the circuit."""

    if circuit_type == 'series':

        total_resistance = np.sum(resistances)

        print( 'The total resistance of this circuit is ' + str(total_resistance) + ' ohms')
        print( 'The voltage of this circuit is ' + str(v_or_a * total_resistance) + ' volts')
        print( 'The amperage of this circuit is ' + str(v_or_a) + ' amps')

    elif circuit_type == 'parallel':

        total_resistance = 0
        for resistance in resistances:
            total_resistance += 1 / resistance # add the reciprocals

        total_resistance = 1 / total_resistance # now take the reciprocal of the sum of the reciprocals

        print( 'The total resistance of this circuit is ' + str(total_resistance) + ' ohms')
        print( 'The voltage of this circuit is ' + str(v_or_a) + ' volts')
        print( 'The amperage of this circuit is ' + str(v_or_a / total_resistance) + ' amps')
    
def piston(V: list, P0: float, V0: float, T0: float, gamma: float) -> list:
    """Returns a (N, 3) list containing (P, V, T) values calculated from the inputted values of V, P0, V0, T0, and gamma, where N equals the length of the inputted list V."""

    P = []
    T = []
    for v in V:
        # use the adiabatic equation to calculate P
        P.append(P0 * (V0 / v) ** gamma)
        # use the ideal gas law to calculate T
        T.append(T0 * (V0 / v) ** (gamma - 1))

    return [P, V, T]