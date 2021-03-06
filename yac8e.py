"""
Copyright (C) 2012-2019 Craig Thomas
This project uses an MIT style license - see LICENSE for details.

A simple Chip 8 emulator - see the README file for more information.
"""
# I M P O R T S ###############################################################

import argparse
import os

# G L O B A L S ###############################################################

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# F U N C T I O N S  ##########################################################


def parse_arguments():
    """
    Parses the command-line arguments passed to the emulator.

    :return: the parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description="Starts a simple Chip 8 "
        "emulator. See README.md for more information, and LICENSE for "
        "terms of use.")
    parser.add_argument(
        "rom", help="the ROM file to load on startup")
    parser.add_argument(
        "--scale", help="the scale factor to apply to the display "
        "(default is 5)", type=int, default=5, dest="scale")
    parser.add_argument(
        "--delay", help="sets the CPU operation to take at least "
        "the specified number of milliseconds to execute (default is 1)",
        type=int, default=1, dest="op_delay")
    return parser.parse_args()


# M A I N #####################################################################

if __name__ == "__main__":
    from chip8.emulator import main_loop
    main_loop(parse_arguments())

# E N D   O F   F I L E #######################################################
