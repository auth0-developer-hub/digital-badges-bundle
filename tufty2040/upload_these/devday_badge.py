# A retro badge with photo and QR code.
# Copy your image to your Tufty alongside this example - it should be a 120 x 120 jpg.

from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from pimoroni import Button
import time
import jpegdec
import qrcode

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
button_b = Button(8, invert=False)
button_c = Button(9, invert=False)

WIDTH, HEIGHT = display.get_bounds()

# Uncomment one of these four colour palettes - find more at lospec.com !
# Devday@Oktane Pallete 1
LIGHTEST = display.create_pen(255,254,250)  # Snow
LIGHT = display.create_pen(177,228,222)  # Turquoise
DARK = display.create_pen(64,22,160)  # Eggplant
DARKEST = display.create_pen(25, 25, 25)  # Carbon

# Devday@Oktane Pallete 2
# LIGHTEST = display.create_pen(246,241,231)  # Cream
# LIGHT = display.create_pen(76,183,163)  # Seafoam
# DARK = display.create_pen(63,89,228)  # Sky
# DARKEST = display.create_pen(25, 25, 25)  # Carbon

BADGE_PATH = "/badges/badge.txt"

# Default text in case the file fails
DEFAULT_TEXT = """Auth0 by Okta
Developer
@developer
Devday@Oktane
okta.com/oktane
/badges/badge.jpg
"""

# Some constants we'll use for drawing
BORDER_SIZE = 4
PADDING = 10
COMPANY_HEIGHT = 40


def draw_badge():
    # draw border
    display.set_pen(LIGHTEST)
    display.clear()

    # draw background
    display.set_pen(DARK)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - (BORDER_SIZE * 2), HEIGHT - (BORDER_SIZE * 2))

    # draw company box
    display.set_pen(DARKEST)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - (BORDER_SIZE * 2), COMPANY_HEIGHT)

    # draw company text
    display.set_pen(LIGHT)
    display.set_font("bitmap6")
    display.text(COMPANY_NAME, BORDER_SIZE + PADDING, BORDER_SIZE + PADDING, WIDTH, 3)

    # draw name text
    display.set_pen(LIGHTEST)
    display.set_font("bitmap8")
    display.text(NAME, BORDER_SIZE + PADDING, BORDER_SIZE + PADDING + COMPANY_HEIGHT, WIDTH, 5)

    # draws the bullet points
    display.set_pen(LIGHT) # Change this to DARKEST if the background is light
    if BLURB1 != "\n":
        display.text(">", BORDER_SIZE + PADDING + 120 + PADDING, 105, 160, 2)
    if BLURB2 != "\n":
        display.text(">", BORDER_SIZE + PADDING + 120 + PADDING, 140, 160, 2)
    if BLURB3 != "\n":
        display.text(">", BORDER_SIZE + PADDING + 120 + PADDING, 175, 160, 2)

    # draws the blurb text (4 - 5 words on each line works best)
    display.set_pen(LIGHTEST)
    display.text(BLURB1, BORDER_SIZE + PADDING + 135 + PADDING, 105, 160, 2)
    display.text(BLURB2, BORDER_SIZE + PADDING + 135 + PADDING, 140, 160, 2)
    display.text(BLURB3, BORDER_SIZE + PADDING + 135 + PADDING, 175, 160, 2)


def show_photo():
    j = jpegdec.JPEG(display)
    # Open the JPEG file
    j.open_file(BADGE_PATH)

    # Draws a box around the image
    display.set_pen(DARKEST)
    display.rectangle(PADDING, HEIGHT - ((BORDER_SIZE * 2) + PADDING) - 120, 120 + (BORDER_SIZE * 2), 120 + (BORDER_SIZE * 2))

    # Decode the JPEG
    j.decode(BORDER_SIZE + PADDING, HEIGHT - (BORDER_SIZE + PADDING) - 120)

    # Draw QR button label
    display.set_pen(LIGHTEST)
    display.text("QR", 240, 215, 160, 2)


def measure_qr_code(size, code):
    w, h = code.get_size()
    module_size = int(size / w)
    return module_size * w, module_size


def draw_qr_code(ox, oy, size, code):
    size, module_size = measure_qr_code(size, code)
    display.set_pen(LIGHTEST)
    display.rectangle(ox, oy, size, size)
    display.set_pen(DARKEST)
    for x in range(size):
        for y in range(size):
            if code.get_module(x, y):
                display.rectangle(ox + x * module_size, oy + y * module_size, module_size, module_size)


def show_qr():
    display.set_pen(DARK)
    display.clear()

    code = qrcode.QRCode()
    code.set_text(QR_TEXT)

    size, module_size = measure_qr_code(HEIGHT, code)
    left = int((WIDTH // 2) - (size // 2))
    top = int((HEIGHT // 2) - (size // 2))
    draw_qr_code(left, top, HEIGHT, code)


# Open the badge file
try:
    badge = open(BADGE_PATH, "r")
except OSError:
    with open(BADGE_PATH, "w") as f:
        f.write(DEFAULT_TEXT)
        f.flush()
    badge = open(BADGE_PATH, "r")


# Read in the next 7 lines
COMPANY_NAME = badge.readline()        # "Auth0 by Okta"
NAME = badge.readline()                # "Developer"
BLURB1 = badge.readline()              # "@developer"
BLURB2 = badge.readline()              # "Devday@Oktane"
BLURB3 = badge.readline()              # "okta.com/oktane"

QR_TEXT = badge.readline()             # ""
BADGE_PATH = badge.readline()          # /badges/badge.jpg


# draw the badge for the first time
badge_mode = "qr"
draw_badge()
show_photo()
display.update()

while True:
    if button_c.is_pressed:
        if badge_mode == "qr":
            badge_mode = "qr"
            show_qr()
            display.update()
            time.sleep(0.1)
            if button_b.is_pressed:
                print("button b")
        else:
            badge_mode = "photo"
            draw_badge()
            show_photo()
            display.update()
        time.sleep(1)
    elif button_b.is_pressed:
        # will re-draw the badge can be used to go back from QR code
        draw_badge()
        show_photo()
        display.update()
        time.sleep(0.1)
