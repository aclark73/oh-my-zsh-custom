#!/usr/bin/env python
"""
Generate colors, usually used to tag things so it should
produce distinct hues and be consistent for a given value.

Much of the original based on
rainbow-parade.py
http://games.adultswim.com/robot-unicorn-attack-twitchy-online-game.html
http://stackoverflow.com/questions/1523427/python-what-is-the-common-header-format
Mikko Ohtamaa <mikko@opensourcehacker.com>
Toholampi http://www.toholampi.fi/tiedostot/119_yleisesite_englanti_naytto.pdf

"""

import colorsys
import sys
import os
import socket
from functools import reduce


def get_random_for_string(name, range):
    """
    Get always the same random number based on an arbitrary string
    """
    # Just sum characters and divide
    sum = reduce(lambda x, y: x + (y * 37), [ord(c) for c in name])
    return sum % range
    # Use the value as a RNG seed and get the first value
    # This doesn't work across systems!
    # random.seed(name)
    # return random.random() * range


def get_hue_for_string(name):
    """
    Get the random number as a hue value (0..1)
    """
    return float(get_random_for_string(name, 360)) / 360


def decorate_terminal(color):
    """
    Set terminal tab / decoration color.

    Please note that iTerm 2 / Konsole have different control codes over this.
    Note sure what other terminals support this behavior.

    :param color: tuple of (r, g, b)
    """

    if color is None:
        # Reset tab color
        sys.stdout.write("\033]6;1;bg;*;default\a")
        sys.stdout.flush()
    else:
        r, g, b = color

        # iTerm 2
        # http://www.iterm2.com/#/section/documentation/escape_codes"
        sys.stdout.write("\033]6;1;bg;red;brightness;%d\a" % int(r * 255))
        sys.stdout.write("\033]6;1;bg;green;brightness;%d\a" % int(g * 255))
        sys.stdout.write("\033]6;1;bg;blue;brightness;%d\a" % int(b * 255))
        sys.stdout.flush()

        # Konsole
        # TODO
        # http://meta.ath0.com/2006/05/24/unix-shell-games-with-kde/


def get_hue_for_path(path):
    """
    Return a hue for a path, it can be overridden by a file on the path
    """
    if os.path.exists("%s/.hue" % path):
        with open("%s/.hue" % path, 'rb') as f:
            hue_name = f.readline().strip()
            if hue_name:
                try:
                    # If it's a number, return that
                    return float(hue_name) / 360
                except ValueError:
                    # Otherwise, treat as the "real" name
                    return get_hue_for_string(hue_name)
    # Default is that the path is the name
    return get_hue_for_string(path)


def set_terminal_color(name, lightness=0.7, saturation=0.7):
    """
    Colorize terminal tab by the current path.

    Create a color in HSL space where lightness and saturation is locked,
    tune only hue.
    """
    if name:
        hue = get_hue_for_path(name)
        color = colorsys.hls_to_rgb(hue, lightness, saturation)
        decorate_terminal(color)
    else:
        decorate_terminal(None)


def print_zsh_color(name):
    """
    Write out a zsh color code
    """
    color = get_random_for_string(name, 255)
    sys.stdout.write("%d" % color)
    sys.stdout.flush()


def main():
    name = socket.gethostname()
    print_zsh_color(name)


if __name__ == "__main__":
    main()
