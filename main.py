Qibla = 0

def on_forever():
    global Qibla
    Qibla = input.compass_heading()
    if Qibla <= 145 and Qibla >= 125:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
