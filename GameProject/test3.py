import getch

import msvcrt
  
while True:
    character = msvcrt.getch()
    print(repr(character))
    if character == b'q':
        break
