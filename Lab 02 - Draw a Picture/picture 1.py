import arcade

arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.color.BARBIE_PINK)
arcade.start_render()

arcade.draw_circle_filled(300, 400, 100, arcade.csscolor.MEDIUM_PURPLE)
arcade.draw_circle_filled(250, 425, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(350, 425, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(335, 425, 15, arcade.csscolor.BLACK)
arcade.draw_circle_filled(265, 425, 15, arcade.csscolor.BLACK)
arcade.draw_arc_filled(300, 350, 60, 100, arcade.csscolor.INDIANRED, 0, 180)

arcade.draw_line(250, 315, 215, 275, arcade.color.PURPLE, 10)
arcade.draw_line(215, 275, 250, 235, arcade.color.PURPLE, 10)
arcade.draw_line(250, 235, 215, 195, arcade.color.PURPLE, 10)

arcade.draw_line(300, 300, 265, 260, arcade.color.PURPLE, 10)
arcade.draw_line(265, 260, 300, 220, arcade.color.PURPLE, 10)
arcade.draw_line(300, 220, 265, 180, arcade.color.PURPLE, 10)

arcade.draw_line(350, 315, 315, 275, arcade.color.PURPLE, 10)
arcade.draw_line(315, 275, 350, 235, arcade.color.PURPLE, 10)
arcade.draw_line(350, 235, 315, 195, arcade.color.PURPLE, 10)

arcade.finish_render()
arcade.run()

