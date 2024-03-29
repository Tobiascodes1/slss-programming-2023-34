BLACK_PIXEL = (0, 0, 0)
DARK_GRAY_PIXEL = (127, 127, 127)
LIGHT_GRAY_PIXEL = (128, 128, 128)
WHITE_PIXEL = (255, 255, 255)


def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 220 and r < 120 and b < 120:
        return "green"
    if g < 90 and b < 90 and r > 150:
        return "red"
    if g >= 80 and b < 50 and r < 50:
        return "jelly bean green"


print(pixel_to_string((160, 0, 4)))  # red
print(pixel_to_string(WHITE_PIXEL))


def is_light(pixel: tuple) -> bool:
    """Returns true if given pixel is "light"

    Params:
        pixel - 3-tuple of values red, green, blue

    Returns:
        True if pixel is light false if not
    """
    return pixel >= (128, 128, 128)


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Returns a grayscale version of the given pixel"""
    gray = int(pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)

    return (gray, gray, gray)