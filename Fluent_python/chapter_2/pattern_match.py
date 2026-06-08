# Pattern Matching with Sequences 
# Method from an imaginary Robot Class 

#  def handle_command(self, message):
#     match message:
#         case ['BEEPER', frequency, times]:
#             self.beep(times, frequency)
#         case ['NECK', angle]:
#             self.rotate_neck(angle)
#         case ['LED', ident, intensity]:
#             self.leds[ident].set_brightness(ident, intensity)
#         case ['LED', ident, red, green, blue]:
#             self.leds[ident].set_color(ident, red, green, blue)
#         case _:
#             raise InvalidCommand(message)


# Destucting nested tuples - 

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),


]

def main():
    print(f"{'':15} | {'lattitide':>9} | {'logitude':>9}")
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


# Line Items from a flat-file invoice 

invoice = """ 

0.....6.................................40........52...55........
1909 Pimoroni PiBrella                      $17.50    3    $52.50
1489 6mm Tactile Switch x20                  $4.95    2    $9.90
1510 Panavise Jr. - PV-201                  $28.00    1    $28.00
1601 PiTFT Mini Kit 320x240                 $34.95    1    $34.95

"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(53, 55)
ITEM_TOTAL = slice(55, None)


line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

    
