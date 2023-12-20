'''import time 
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}: {02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
    print("Timer done")'''
    
import time
import termios

def countdown(t):
    # Get terminal width and move cursor to starting position
    width, _ = termios.get_terminal_size()
    print("\r", end=" "*width)
    print("\r", end="")

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}: {:02d}'.format(mins, secs)
        # Clear timer area and print with custom color
        print("\r", end=" "*len(timer))
        print("\r" + timer, end="", flush=True)
        time.sleep(1)
        t -= 1

    print("\rTimer done", end="")

countdown(60)
