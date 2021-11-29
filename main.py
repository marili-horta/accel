def on_button_pressed_a():
    global attivo
    attivo = not (attivo)
    if attivo:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

attivo = False
attivo = False
basic.show_icon(IconNames.NO)

def on_forever():
    if attivo:
        serial.write_numbers([input.acceleration(Dimension.X),
                input.acceleration(Dimension.Y),
                input.acceleration(Dimension.Z)])
basic.forever(on_forever)
