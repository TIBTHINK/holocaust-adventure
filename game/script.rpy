# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("A dirty jew")
define g = Character("Guard")
define e1 = Character("A-7713")
define e2 = Character("Elie")


# The game starts here.

# label splashscreen:
#     scene black
#     with Pause(1)
#
#     show text "Tibthink Productions Presents..." with dissolve
#     with Pause(2)
#
#     hide text with dissolve
#     with Pause(1)
#
#     return


image black = "#000"
image white = "#ffffff"
image logo = "images/logo/icon-left-font-monochrome-black.png"

transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform transform_white:
    on show:
        alpha 0
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

label splashscreen:
    scene black
    $ renpy.pause(1, hard=True)

    show white at transform_white
    $ renpy.pause(2, hard=True)

    show logo at transform_logo
    $ renpy.pause(6, hard=True)

    hide logo
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(3, hard=True)

    with Pause(1)

    show text "Warning: \n Tibthink does not give two shits about what you think and what you believe.\n If you can not take a joke please read the word below. \n FUCK YOU"
    with Pause(7)

    hide text with dissolve
    with Pause(1)

    return

label disclaimer:



label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene auschwitz

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    e "Please kill me"
    show Guard
    g "not today [e1]"

    # This ends the game.

    return
