# Functions...

# Colours text
def colorize(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color.lower(), '')}{text}{colors['reset']}"


# Main Routine...

# Example usage of colorize function
word = "code"
ask = input(colorize(f"How do you like to {word}?", "red"))
