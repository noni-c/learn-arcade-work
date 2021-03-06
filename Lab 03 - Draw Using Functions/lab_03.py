import arcade

arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.color.FRENCH_SKY_BLUE)

arcade.start_render()
# mountain
arcade.draw_triangle_filled(0, 300, 250, 550, 500, 300, arcade.csscolor.DIM_GRAY)
arcade.draw_triangle_filled(100, 300, 250, 550, 500, 300, arcade.csscolor.DARK_GRAY)

# ground
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.GREEN)

# trees
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_triangle_filled(500, 500, 450, 320, 550, 320, arcade.csscolor.DARK_GREEN)

# pond
arcade.draw_ellipse_filled(300, 200, 400, 100, arcade.color.FRENCH_SKY_BLUE)

# sun!
arcade.draw_circle_filled(500, 550, 30, arcade.csscolor.GOLD)
arcade.draw_circle_filled(485, 550, 5, arcade.csscolor.BLACK)
arcade.draw_circle_filled(515, 550, 5, arcade.csscolor.BLACK)
arcade.draw_arc_filled(500, 535, 10, 10, arcade.csscolor.BLACK, 0, 180)

arcade.finish_render()
arcade.run()
