input.onButtonPressed(Button.A, function () {
    attivo = !(attivo)
    if (attivo) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
let attivo = false
attivo = false
basic.showIcon(IconNames.No)
basic.forever(function () {
    if (attivo) {
        serial.writeNumbers([input.acceleration(Dimension.X), input.acceleration(Dimension.Y), input.acceleration(Dimension.Z)])
    }
})
