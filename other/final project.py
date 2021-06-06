import arcade


def information_rules():
    # print the rules and how to play
    repetition = int(input("how many times do you want the rules printed? "))
    for i in range(repetition):
        print("1. close the title window when you're ready to play")
        print("2. it's a very simple trivia game")
        print("3. enter answer letter when prompted in lowercase")
        print("4. that's pretty much it, you got this!")


def title_text():
    # prints the title text
    print("")
    print("trivia time!")


def main():
    # question 1
    print("")
    print("question 1: what's the biggest island in the world?")
    print("a. greenland")
    print("b. australia")
    print("c. madagascar")
    print("d. iceland")
    answer_one = input("answer: ")

    # tracking the scores
    total_score = 0

    if answer_one.lower() == "a":
        print("correct!")
        total_score += 1
        print("overall score:", total_score)
    else:
        print("incorrect.")
        print("correct answer: greenland")
        print("overall score:", total_score)

    # question 2
    print("")
    print("question 2: what's the hottest planet in the solar system?")
    print("a. jupiter")
    print("b. mercury")
    print("c. venus")
    print("d. mars")
    answer_two = input("answer: ")

    if answer_two.lower() == "c":
        print("correct!")
        total_score += 1
        print("overall score:", total_score)
    else:
        print("incorrect.")
        print("correct answer: venus")
        print("overall score:", total_score)

    # question 3
    print("")
    print("question 3: what was google's original name?")
    print("a. BackRub")
    print("b. WebCatalog")
    print("c. WebPortal")
    print("d. BackWebs")
    answer_three = input("answer: ")

    if answer_three.lower() == "a":
        print("correct!")
        total_score += 1
        print("overall score:", total_score)
    else:
        print("incorrect.")
        print("correct answer: BackRub")
        print("overall score:", total_score)

    # question 4
    print("")
    print("question 4: who was the first woman to win a nobel prize?")
    print("a. serena williams")
    print("b. ada lovelace")
    print("c. malala yousafzai")
    print("d. marie curie")
    answer_four = input("answer: ")

    if answer_four.lower() == "d":
        print("correct!")
        total_score += 1
        print("overall score:", total_score)
    else:
        print("incorrect.")
        print("correct answer: marie curie")
        print("overall score:", total_score)

    # question 5
    print("")
    print("question 5: what country invented tea?")
    print("a. united kingdom")
    print("b. china")
    print("c. united states of america")
    print("d. germany")
    answer_five = input("answer: ")

    if answer_five.lower() == "b":
        print("correct!")
        total_score += 1
        print("overall score:", total_score)
    else:
        print("incorrect.")
        print("correct answer: china")
        print("overall score:", total_score)

    # gives total score
    print("")
    print("your total score was: ", total_score, "/ 5")


def title_screen():
    # opens the title screen
    arcade.open_window(600, 600, "title screen")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    # draw title
    arcade.draw_text("Trivia Time!", 225, 480, arcade.csscolor.CHARTREUSE, 24)
    arcade.draw_rectangle_outline(300, 500, 300, 100, arcade.csscolor.CHARTREUSE, 25)
    arcade.draw_rectangle_outline(300, 500, 375, 175, arcade.csscolor.CYAN, 25)

    # draw confetti
    arcade.draw_rectangle_filled(50, 500, 10, 15, arcade.csscolor.WHITE, 25)
    arcade.draw_rectangle_filled(75, 200, 10, 15, arcade.csscolor.WHITE, 75)
    arcade.draw_rectangle_filled(500, 350, 10, 15, arcade.csscolor.WHITE, 175)
    arcade.draw_rectangle_filled(575, 100, 10, 15, arcade.csscolor.WHITE, 35)
    arcade.draw_rectangle_filled(300, 300, 10, 15, arcade.csscolor.WHITE, 60)
    arcade.draw_rectangle_filled(200, 250, 10, 15, arcade.csscolor.WHITE, 10)
    arcade.draw_rectangle_filled(350, 100, 10, 15, arcade.csscolor.WHITE, 75)
    arcade.draw_rectangle_filled(200, 50, 10, 15, arcade.csscolor.WHITE, 35)
    arcade.draw_rectangle_filled(175, 400, 10, 15, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(550, 550, 10, 15, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(550, 200, 10, 15, arcade.csscolor.WHITE, 95)

    # draw exit instructions
    arcade.draw_text("press the x to start game", 175, 200, arcade.csscolor.WHITE, 18)

    arcade.finish_render()
    arcade.run()


def end_game():
    # prints the end game info
    print("")
    print("game over!")
    print("good job and thanks for playing!")


information_rules()
title_screen()
title_text()
main()
end_game()
