let Qibla = 0
basic.forever(function () {
    Qibla = input.compassHeading()
    if (Qibla <= 145 && Qibla >= 125) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
