import curses
from PIL import Image
from pokedex.image_handler import ImageHandler

class Menu:
    
    def __init__(self, name, window_y = 60, window_x = 90):
        self.name = name
        self.window_x = window_x
        self.window_y = window_y
        self.menu_dict = {}
        self.current_row = 0
        self.initialized_colors = 50
        self.initialized_color_pairs = 2
    
    def run(self, stdscr):
        curses.start_color()    
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.curs_set(0)
        

        self.stdscr = stdscr
        # Loop to handle user input
        while True:
            #break from loop on exit
            self._display()
            self._handle_input()

    def add_menu_dict_option(self, key, value):
        self.menu_dict[key] = value

    def print_string(self, x, y, print, color_pair):
        self.stdscr.attron(curses.color_pair(color_pair))
        self.stdscr.addstr(y, x, print)
        self.stdscr.attroff(curses.color_pair(color_pair))

    def _display(self):
        
        curses.resize_term(self.window_y, self.window_x)
        self.stdscr.clear()
        x_space = 4
        y_space = 2
        ImageHandler.print_file(self, "461.gif")


        for i, item in enumerate(self.menu_dict.keys()):
            if i == self.current_row:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y_space + i, x_space, self.name + "> " + item)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y_space + i, x_space, item)
        
        self.stdscr.refresh()
        
    def _handle_input(self):
 
        key = self.stdscr.getch()
        
        if key == curses.KEY_UP and self.current_row > 0:
            self.current_row -= 1
        elif key == curses.KEY_DOWN and self.current_row < len(self.menu_dict.keys()) - 1:
            self.current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            menu_key = list(self.menu_dict.keys())[self.current_row]
            self.menu_dict[menu_key](self.stdscr)

        