"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
import turtle
import pandas as pd
import struct
import imghdr


IMAGE = 'blank_states_img.gif'
CSV = f'coord_selected_in_{IMAGE}.csv'


def get_gif_size(file_name):
    """
    Returns .gif image size
    """
    with open(file_name, 'rb') as file_handle:
        if len(head := file_handle.read(24)) != 24:
            return
        elif imghdr.what(file_name) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
    return width, height


def get_mouse_click_coord(x, y):
    """
    Populates a dataFrame with the data from the image loaded as a turtle.
    """
    pd.DataFrame({
            'state_name': [input('StaTe: ')],
            'coord_x': x,
            'coord_y': y
    }).to_csv(CSV, mode='a', header=False)
    print(x, y)


if __name__ == '__main__':

    with open(CSV, 'w'):
        # Opens file stored in CSV constant  in order to wipe it if it already exists.
        pass

    size = get_gif_size(IMAGE)
    window = turtle.Screen()
    window.setup(size)
    pd.DataFrame({'state_name': [],
                  'coord_x': [],
                  'coord_y': []}).to_csv(CSV, mode='a')
    window.onscreenclick(get_mouse_click_coord)
    window.title('Coord Selector')
    window.addshape(IMAGE)
    turtle.shape(IMAGE)

    window.tracer(0)

    turtle.mainloop()
