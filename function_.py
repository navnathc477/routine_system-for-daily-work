from PIL import Image
from screeninfo import get_monitors

def get_geometry(root):
    root.resizable(False, False)
    root.state('zoomed')
    get_mon = get_monitor()
    monitor = str(get_mon[0]) + "x" + str(get_mon[1])
    root.geometry(monitor)

def get_monitor():
    for m in get_monitors():
        width = m.width
        heigth = m.height
        return width, heigth

def resize_custom(str, x, y):
    image = Image.open(str)
    image = image.resize((x, y), Image.ANTIALIAS)
    return image