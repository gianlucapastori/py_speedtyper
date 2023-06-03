import curses 
import time 
import random
from data import Data, Keys

class Typer:
    def __init__(self) -> None:
        # variable initialization.
        # curses related.
        self.stdscr: curses.window = curses.initscr()
        self.heigth, self.widtht = self.stdscr.getmaxyx()
        # typer related.
        self.set_array = []
        self.typed_array = []
        self.state = 0
        self.set_number = 16
        self.lang = "en"
        self.array_words = []
        self.timer = 0
        self.start_time = 0
        self.end_time = 0
        self.finished = 0
        self.uncorrected_errors = 0
        # data related.
        self.keys = Keys()
        self.data = Data()

        # curses initialization and setup.
        # do not echo last character.
        curses.noecho()             
        # do not show terminal cursor.
        curses.curs_set(0)         
        # check if terminal support colors.
        if curses.has_colors():
            curses.start_color()
            curses.use_default_colors()
            # 1 = white on black // default and typed
            # 2 = grey on black  // non-typed
            # 3 = red on black   // error
            # 4 = blue on black  // special
            # 5 = black on white // cursor
            # reference: https://i.stack.imgur.com/KTSQa.png
            curses.init_pair(1, 15, -1)
            curses.init_pair(2, 7, -1)
            curses.init_pair(3, 9, 255)
            curses.init_pair(4, 6, -1)
            curses.init_pair(4, 0, 255)

    def on_key(self, ch) -> None:
        if ch == self.keys.esc:
            exit()

        if self.state == 0:
            if ch == self.keys.num_1:
                self.state = 1
            elif ch == self.keys.num_2:
                self.state = 2
        elif self.state == 1:
            self.populate_typed(ch)
            if ch == self.keys.num_2:
                self.stdscr.addstr("\n\ntime: {}\nuncorrected errors: {}\n\n".format(self.timer,self.uncorrected_errors))
        elif self.state == 2:
            if ch == self.keys.num_1:
                self.change_lang("en")
                self.state = 0
            elif ch == self.keys.num_2:
                self.change_lang("br")
                self.state = 0
                        

    def on_tick(self, time) -> None:
        if self.state == 1:
            self.typer_tick(time)

    def typer_tick(self, time) -> None:
        if len(self.typed_array):
            if self.start_time == 0:
                self.start_time = time
        if len(self.typed_array) == len(self.set_array):
            self.timer = abs(self.start_time - time)
            for i in range(len(self.set_array)):
                if self.typed_array[i] != self.set_array[i]:
                    self.uncorrected_errors += 1
            self.state = 3
    
    def on_draw(self) -> None:
        if self.state == 0:
            self.draw_menu()
        elif self.state == 1:
            self.draw_typer()
        elif self.state == 2:
            self.draw_lang_selection()
        elif self.state == 3:
            self.draw_finish()

    def draw_finish(self) -> None:
        self.stdscr.addstr("your completed the test!\n")
        self.stdscr.addstr("the time it take: {}\n".format(self.timer))
        self.stdscr.addstr("your uncorrected errors: {}\n".format(self.uncorrected_errors))
        
        gross, net, accuracy = self.calculate_wpm()
        
        self.stdscr.addstr("your gross WPM: {}\n".format(gross))
        self.stdscr.addstr("your net WPM: {}\n".format(net))
        self.stdscr.addstr("your accuracy: {}%\n".format(accuracy))
        self.stdscr.addstr("your accuracy: {}%\n".format(len(self.typed_array)))
        
        self.stdscr.addstr("\n")
        
        if net > 10 and net < 20:
            self.stdscr.addstr("really really bad at typing :D")
        elif net > 20 and net < 30:
            self.stdscr.addstr("really bad at typing D:")
        elif net > 30 and net < 40:
            self.stdscr.addstr("bad at typing :(")
        elif net > 40 and net < 50:
            self.stdscr.addstr("youre the average typist, still bad.")
        elif net > 50 and net < 60:
            self.stdscr.addstr("yeah! your above average! congratualations!")
        elif net > 60 and net < 70:
            self.stdscr.addstr("the required speed for most job, a professional typer, indeed...")
        elif net > 70 and net < 80:
            self.stdscr.addstr("youre good good :)")
        elif net > 80 and net < 90:
            self.stdscr.addstr("youre very very god :O")
        else:
            self.stdscr.addstr("youre a god at typing")
    
    def calculate_wpm(self) -> (float, float, float):
        gross = (len(self.typed_array) / 5) / (abs(self.timer / 60))
        net = ((gross - self.uncorrected_errors) / (self.timer / 60))
        accuracy = ((len(self.typed_array) / self.uncorrected_errors) * 100)
        
        return gross, net, accuracy
        
    def draw_typer(self) -> None:
        for i in range(len(self.set_array)):
            if i == len(self.typed_array):
                self.stdscr.addstr(str(self.set_array[i]), curses.color_pair(4))
                continue
            if len(self.typed_array) > i:
                if self.typed_array[i] == self.set_array[i]:
                    self.stdscr.addstr(str(self.set_array[i]))
                else:
                    self.stdscr.addstr(str(self.set_array[i]), curses.color_pair(3))
            else:
                self.stdscr.addstr(str(self.set_array[i]), curses.color_pair(2))
        
        if len(self.typed_array) == 0:
            self.stdscr.addstr("\n\nthe timer will start when you start typing, and it will stop when you finish the set.")

    def draw_menu(self) -> None:
        self.stdscr.addstr("created by gianlucapastori\n")
        self.stdscr.addstr("welcome to")
        self.stdscr.addstr(" speedtyper! ", curses.color_pair(3))
        self.stdscr.addstr("what do you want do do?\n")
        self.stdscr.addstr("(1). Start Words per Minute Typing Test\n")
        self.stdscr.addstr("(2). Change test language ({})\n".format(str(self.lang)))
        self.stdscr.addstr("(3). cat README.md\n")
        self.stdscr.addstr("(ESC). exit\n")

    def populate_typed(self, ch) -> None:
        if ch in self.keys.alphabet:
            self.typed_array.append(str(chr(ch)))
        if ch == self.keys.space:
            self.typed_array.append(" ")
        if ch in self.keys.backspace:
            self.typed_array.pop()

    def populate_set(self) -> None:
        self.set_array = []
        if self.lang == "en":
            self.array_words = self.data.en_words
        elif self.lang == "br":
            self.array_words = self.data.br_words

        for i in range(self.set_number):
            word = self.array_words[random.randint(0, len(self.array_words) - 1)] 
            for j in range(len(word)):
                letter = word[j]
                self.set_array.append(letter)

            self.set_array.append(" ")
            
        self.set_array.pop()

    def draw_lang_selection(self) -> None:
        self.stdscr.addstr("select the language you want to make the test.\n")
        self.stdscr.addstr("(just the data set of the test will be affected):\n")
        self.stdscr.addstr("(1). en_US\n")
        self.stdscr.addstr("(2). pt_BR\n")

    def change_lang(self, lang) -> None:
        self.lang = lang
        self.populate_set()

    def loop(self) -> None:
        self.stdscr.erase()

        ch = -1

        self.populate_set()

        # main loop.
        while True:
            self.stdscr.erase()
            self.on_key(ch)
            self.on_draw()
            self.on_tick(time.time())
            ch = self.stdscr.getch()
