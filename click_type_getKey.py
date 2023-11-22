'''
Author name: Jeremiah E. Ochepo
Last Edited: 2/15/2020 (7 PM)
Description: Click then Type
'''

from graphics import *


def click_then_type():
    # Create a graphics window
    win = GraphWin('Click on a diagonal point', 400, 400)

    # Display initial message
    message = Text(Point(200, 20), 'Click any Points').draw(win)

    # Allow the user to click and type five times
    for _ in range(5):
        # Get a click point
        click_point = win.getMouse()

        # Get a key press
        key = win.getKey()

        # Display the key at the click point
        label = Text(click_point, key)
        label.draw(win)

    # Close the window when done
    win.getMouse()
    win.close()


if __name__ == "__main__":
    click_then_type()
