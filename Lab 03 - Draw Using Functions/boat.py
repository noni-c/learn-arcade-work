import arcade

arcade.open_window(600, 600, "super cool boat!")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()


def print_ocean():
    # we are printing an ocean !!
    arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.csscolor.STEEL_BLUE)


def print_boat():
    # we are printing a boat !!
    arcade.draw_arc_filled(300, 225, 150, 100, arcade.csscolor.PERU, 0, 180, 180)


def print_sail():
    # we are printing the pole and sail !!
    arcade.draw_line(270, 225, 270, 350, arcade.csscolor.PERU, 10)
    arcade.draw_triangle_filled(277, 230, 277, 350, 350, 230, arcade.csscolor.WHITE)


def print_sun():
    # we are printing a sun !!
    arcade.draw_circle_filled(500, 500, 40, arcade.csscolor.GOLD)


def print_cloud():
    # clouds yuh !!
    arcade.draw_ellipse_filled(375, 475, 100, 50, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(345, 450, 100, 50, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(405, 450, 100, 50, arcade.csscolor.WHITE)


def print_second_cloud():
    # cloud 2 !!
    arcade.draw_ellipse_filled(175, 375, 100, 50, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(145, 350, 100, 50, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(205, 350, 100, 50, arcade.csscolor.WHITE)


def print_bubble(x, y):
    arcade.draw_circle_outline(x, y, 10, arcade.csscolor.LIGHT_STEEL_BLUE, 2)

print_boat()
print_ocean()
print_sail()
print_sun()
print_cloud()
print_second_cloud()
print_bubble(100, 100)
print_bubble(200, 50)
print_bubble(350, 150)
print_bubble(550, 50)

arcade.finish_render()
arcade.run()