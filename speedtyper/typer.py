import curses 
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
        self.set_number = 15
        self.lang = "default"
        self.array_words = []
        # data related.
        self.keys = Keys()
        self.data = Data()

        # curses initialization and setup.
        # do not echo last character.
        curses.noecho()             
        # do not show terminal cursor.
        curses.curs_set(0)         
        # delay to capture escape key.
        curses.set_escdelay(1)    
        # check if terminal support colors.
        if curses.has_colors():
            curses.start_color()
            curses.use_default_colors()
            # 1 = white on black // default and typed
            # 2 = grey on black  // non-typed
            # 3 = red on black   // error
            # 4 = blue on black  // special
            # reference: https://i.stack.imgur.com/KTSQa.png
            curses.init_pair(1, 15, -1)
            curses.init_pair(2, 7, -1)
            curses.init_pair(3, 9, -1)
            curses.init_pair(4, 6, -1)

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
        elif self.state == 2:
            if ch == self.keys.num_1:
                self.change_lang("en")
            elif ch == self.keys.num_2:
                self.change_lang("br")

    def draw(self) -> None:
        if self.state == 0:
            self.draw_menu()
        elif self.state == 1:
            self.draw_typer()
        elif self.state == 2:
            self.draw_lang_selection()

    def draw_typer(self) -> None:
        for i in range(len(self.set_array)):
            self.stdscr.addstr(str(self.set_array[i]))

    def draw_menu(self) -> None:
        self.stdscr.addstr("created by gianlucapastori\n")
        self.stdscr.addstr("welcome to")
        self.stdscr.addstr(" speedtyper! ", curses.color_pair(4))
        self.stdscr.addstr("what do you want do do?\n")

        self.stdscr.addstr("(1). Start Words per Minute Typing Test\n")
        self.stdscr.addstr("(2). Change test language\n")
        self.stdscr.addstr("(3). cat README.md\n")
        self.stdscr.addstr("(ESC). exit\n")

    def populate_typed(self, ch) -> None:
        if ch in self.keys.alphabet:
            self.typed_array.append(str(ch))
        if ch == self.keys.space:
            self.typed_array.append(" ")
        if ch == self.keys.backspace:
            self.typed_array.pop()

    def populate_set(self) -> None:
        if self.lang == "default" or self.lang == "en":
            self.array_words = self.data.en_words
        elif self.lang == "br":
            self.array_words = self.data.br_words

        for i in range(self.set_number):
            word = self.array_words[random.randint(0, len(self.array_words) - 1)] 
            for j in range(len(word)):
                letter = word[j]
                self.typed_array.append(letter)

            if i != 0 or i != self.set_number:
                self.typed_array.append(" ")

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
            self.draw()
            ch = self.stdscr.getch()
