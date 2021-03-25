import arcade

arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.ALICE_BLUE)

arcade.start_render()

# flag pole
arcade.draw_lrtb_rectangle_filled(50, 80, 550, 0, arcade.csscolor.GRAY)

# hill
arcade.draw_ellipse_filled(300, 0, 600, 200, arcade.csscolor.GREEN, 0)

# japanese flag
arcade.draw_lrtb_rectangle_filled(60, 450, 570, 370, arcade.csscolor.WHITE)
arcade.draw_circle_filled(255, 470, 60, arcade.csscolor.RED)

# flower
arcade.draw_line(300, 100, 300, 150, arcade.csscolor.GREEN, 5)

arcade.finish_render()
arcade.run()