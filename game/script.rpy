# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("A dirty jew")
define g = Character("Guard")
define e1 = Character("A-7713")
define e2 = Character("Elie")


# The game starts here.

label splashscreen:
    scene black
    with Pause(1)

    show text "Tibthink Studios Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

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
