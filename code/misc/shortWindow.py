import numpy


def strategy(history, memory):
    """
    Check the last 4 moves. Defect if 2 or more were defections.
    """
    num_rounds = history.shape[1]
    if num_rounds < 4:
        return 1, None

    window_start = num_rounds - 4
    window_end = num_rounds
    their_recent_moves = history[1, window_start:window_end]
    their_recent_stats = numpy.bincount(their_recent_moves, minlength=1)
    num_defections = their_recent_stats[0]
    if num_defections >= 2:
        choice = 0
    else:
        choice = 1
    return choice, None
