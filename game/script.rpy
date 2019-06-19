define e = Character("A dirty jew")
define g = Character("Guard")
define e1 = Character("A-7713")
define e2 = Character("Elie")



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

    show text "Warning: \n Tibthink does not give two shits about what you think and what you believe.\n If you can not take a joke please read the word below. \n FUCK OFF"
    with Pause(7)

    hide text with dissolve
    with Pause(1)

    return

label disclaimer:



label start:

    play music "audio/null.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene auschwitz

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    e "is there a god"
    menu :
        
        "yes":
            jump thereisag
        "no":
            jump thereisnog

    label thereisag:
        e1 "you are dumber than the last player then"
        call splashscreen
        return

    label thereisnog:
        e1 "hi my name is [e2]"
        

    # This ends the game.
    call credits
    return


label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('Backgrounds', 'Tibthink'), ('Backgrounds', 'Google'), ('Sprites and CG', 'Kirbyhatesyou'), ('Writing', 'Interactive_darkness'), ('Programming', 'Tibthink'), ('Music', 'Youtube'), ('Suggested by: ','Ben.x14'), ('Suggested by: ', 'You honest to goodness cunt')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.3.0.271" #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)