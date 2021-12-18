from random import shuffle


class Playgame:
    global deck_size, suits, values
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.newcardset = []
        self.newcardset2 = []

    def create_deck(self):
        for i in suits:
            for j in values:
                self.newcardset.append(j)
                self.newcardset2.append(i)

    def shuffle_number(self):
        if len(self.newcardset) < 52:
            print("Cant shuffle the cards")

        else:
            shuffle(self.newcardset)
            return self.newcardset

    def shuffle_shapes(self):
        if len(self.newcardset2) < 52:
            print("Cant shuffle the cards")

        else:
            shuffle(self.newcardset2)
            return self.newcardset2

    def drawCard_number(self):
        if len(self.newcardset) == 0:
            return "No cards can be poped"

        else:
            get_number = self.newcardset.pop()
            return get_number

    def drawCard_shapes(self):
        if len(self.newcardset2) == 0:
            return "No cards can be poped"

        else:
            get_shapes = self.newcardset2.pop()
            return get_shapes

    def convert_num(self, value):
        num_chr = value
        if (num_chr == 'A'):
            num_int = 10
            return num_int

        elif (num_chr == '2'):
            num_int = 2
            return num_int

        elif (num_chr == '3'):
            num_int = 3
            return num_int

        elif (num_chr == '4'):
            num_int = 4
            return num_int

        elif (num_chr == '5'):
            num_int = 5
            return num_int

        elif (num_chr == '6'):
            num_int = 6
            return num_int

        elif (num_chr == '7'):
            num_int = 7
            return num_int

        elif (num_chr == '8'):
            num_int = 8
            return num_int

        elif (num_chr == '9'):
            num_int = 9
            return num_int

        else:
            num_int = 10
            return num_int

    def ask_user(self):
        choice = input("\n\tDo you want to draw onw more card? y/n: ")
        if (choice == 'y' or choice == 'Y'):
            return True

        else:
            return False

    def user_playAgain(self):
        choice = input("\n\tDo you want to play again? y/n: ")
        if (choice == 'y' or choice == 'Y'):
            return True

        else:
            return False


class userMenu:
    def __init__(self):
        self.playGame = Playgame()

        self.player_value = []
        self.player_number = []
        self.player_mark = []
        self.computer_value = []
        self.computer_number = []
        self.computer_mark = []

        self.player_counter = 0
        self.comp_counter = 0
        self.player_total = 0
        self.comp_total = 0

        self.game_check = True
        self.player_check = True
        self.comp_check = True
        self.main_check = True

    def mainMenu(self):

        while(self.main_check != False):
            self.set_deck()
            self.shuffle_Num()
            self.shuffle_Mark()

            print("\n\tThe Player\tThe Computer")

            while(self.game_check != False):
                if(self.player_check != False):
                    draw_num = self.draw_NumCard()
                    draw_shape = self.draw_MarkCard()
                    print('\t{} {}'.format(draw_num, draw_shape))

                    self.player_total = self.player_total + \
                        self.int_number(draw_num)

                    # self.player_value.append(self.int_number(
                    #     draw_num))
                    self.player_number.append(draw_num)
                    self.player_mark.append(draw_shape)

                    self.player_counter = self.player_counter + 1

                    # for x in range(self.player_counter):
                    #     self.player_total = self.player_total + \
                    #         self.player_value[x]

                    if (self.player_total > 21):
                        self.player_total = 0
                        self.player_check = False

                if (self.comp_check != False):
                    comp_drawNum = self.draw_NumCard()
                    comp_drawShape = self.draw_MarkCard()
                    print('\t\t\t{} {}'.format(comp_drawNum, comp_drawShape))

                    self.comp_total = self.comp_total + \
                        self.int_number(comp_drawNum)

                    # self.computer_value.append(self.int_number(
                    #     comp_drawNum))
                    self.computer_number.append(comp_drawNum)
                    self.computer_mark.append(comp_drawShape)

                    self.comp_counter = self.comp_counter + 1

                    # for x in range(self.comp_counter):
                    #     self.comp_total = self.comp_total + \
                    #         self.computer_value[x]

                    if(self.comp_total >= 15):
                        if(self.comp_total > 21):
                            self.comp_total = 0
                            self.comp_check = False

                        else:
                            self.comp_check = False

                if (self.player_check == True):
                    self.player_check = self.user_choice()

                if (self.player_check == False and self.comp_check == False):
                    self.game_check = False

            print("\n\t----- Result -----")
            print("\tThe Player\tThe Computer")
            if(self.comp_counter > self.player_counter):
                for i in range(self.player_counter):
                    print("\t{} {}\t{} {}".format(
                        self.player_number[i], self.player_mark[i], self.computer_number[i], self.computer_mark[i]))

                for j in range(self.player_counter, self.comp_counter):
                    print("\t\t\t{} {}".format(
                        self.computer_number[j], self.computer_mark[j]))

                print("\n\tScore: {}\tScore: {}".format(
                    self.player_total, self.comp_total))

            if(self.comp_counter < self.player_counter):
                for i in range(self.comp_counter):
                    print("\t{} {}\t{} {}".format(
                        self.player_number[i], self.player_mark[i], self.computer_number[i], self.computer_mark[i]))

                for j in range(self.comp_counter, self.player_counter):
                    print("\t{} {}".format(
                        self.player_number[j], self.player_mark[j]))

                print("\n\tScore: {}\tScore: {}".format(
                    self.player_total, self.comp_total))

            if(self.player_counter == self.comp_counter):
                for i in range(self.player_counter):
                    print("\t{} {}\t{} {}".format(
                        self.player_number[i], self.player_mark[i], self.computer_number[i], self.computer_mark[i]))

                print("\n\tScore: {}\tScore: {}".format(
                    self.player_total, self.comp_total))

            if (self.player_total > self.comp_total):
                print("\n\tGood, you won againt computer!")

            if (self.player_total < self.comp_total):
                print("\n\tSorry, you lost...")

            if (self.main_check):
                self.main_check = self.play_again()

            if (self.main_check):
                self.game_check = True
                self.comp_check = True
                self.player_check = True
                self.player_counter = 0
                self.comp_counter = 0
                self.comp_total = 0
                self.player_total = 0
                self.player_number.clear()
                self.player_mark.clear()
                self.computer_number.clear()
                self.computer_mark.clear()

    def set_deck(self):
        try:
            self.playGame.create_deck()
        except Exception as e:
            print(str(e))

    def shuffle_Num(self):
        try:
            return self.playGame.shuffle_number()

        except Exception as e:
            print(str(e))

    def shuffle_Mark(self):
        try:
            return self.playGame.shuffle_shapes()

        except Exception as e:
            print(str(e))

    def draw_NumCard(self):
        try:
            return self.playGame.drawCard_number()

        except Exception as e:
            print(str(e))

    def draw_MarkCard(self):
        try:
            return self.playGame.drawCard_shapes()

        except Exception as e:
            print(str(e))

    def int_number(self, value):
        try:
            return self.playGame.convert_num(value)

        except Exception as e:
            print(str(e))

    def user_choice(self):
        try:
            return self.playGame.ask_user()

        except Exception as e:
            print(str(e))

    def play_again(self):
        try:
            return self.playGame.user_playAgain()

        except Exception as e:
            print(str(e))


def main():

    playBJ = userMenu()
    playBJ.mainMenu()


main()
