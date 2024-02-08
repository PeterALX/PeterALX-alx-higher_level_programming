
import os
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Call the function to clear the console
clear_console()
s = Square(10, (10, 10))
for i in range(0, 10):
    clear_console()
    s.position = (s.position[0] + 1, s.position[1] + 1)
    s.my_print()
    time.sleep(0.2)
