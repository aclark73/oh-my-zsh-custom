#!/usr/bin/env python
"""

       Set terminal tab / decoration color by the server name.

       Get a random colour which matches the server name and use it for the tab colour:
       the benefit is that each server gets a distinct color which you do not need
       to configure beforehand.

"""

import colorsys
import sys
import os
from functools import reduce

# http://stackoverflow.com/questions/1523427/python-what-is-the-common-header-format
__copyright__ = "Copyright 2012 Mikko Ohtamaa - http://opensourcehacker.com"
__author__ = "Mikko Ohtamaa <mikko@opensourcehacker.com>"
__licence__ = "WTFPL"
__credits__ = ["Antti Haapala"]

USAGE = """
Colorize terminal tab based on the current host name.

Usage: rainbow-parade.py [0-1.0] [0-1.0] # Lightness and saturation values

An iTerm 2 example (recolorize dark grey background and black text):

    rainbow-parade.py 0.7 0.4
"""

def get_hue_by_string(s):
    hue = float(s)/360
    return hue

def get_random_by_string(s):
    """
    Get always the same 0...1 random number based on an arbitrary string
    """
    sum = reduce(lambda x, y: x+(y*37), [ord(c) for c in s])
    return float(sum % 360) / 360
    # Initialize random gen by server name hash
    #random.seed(s)
    #return random.random()


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


def rainbow_unicorn(name, lightness, saturation):
    """
    Colorize terminal tab by your server name.

    Create a color in HSL space where lightness and saturation is locked, tune only hue by the server.

    http://games.adultswim.com/robot-unicorn-attack-twitchy-online-game.html
    """

    # name = socket.gethostname()
    # name = os.getenv('VIRTUAL_ENV')
    if name:
        hue_name = None
        if os.path.exists("%s/.hue" % name):
            with open("%s/.hue" % name, 'rb') as f:
                hue_name = f.readline().strip()
        if hue_name:
            hue = get_hue_by_string(hue_name)
        else:
            hue = get_random_by_string(name)
        color = colorsys.hls_to_rgb(hue, lightness, saturation)
        decorate_terminal(color)
    else:
        decorate_terminal(None)


def main():
    """
    From Toholampi with love http://www.toholampi.fi/tiedostot/119_yleisesite_englanti_naytto.pdf
    """
    #if len(sys.argv) == 1:
    #    sys.exit(USAGE)

    name = None
    lightness = 0.7
    saturation = 0.7
    if len(sys.argv) > 1:
        name = sys.argv[1]
    if len(sys.argv) > 2:
        lightness = float(sys.argv[2])
    if len(sys.argv) > 3:
        saturation = float(sys.argv[3])

    rainbow_unicorn(name, lightness, saturation)


if __name__ == "__main__":
    main()
