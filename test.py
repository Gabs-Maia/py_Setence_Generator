import format_text
import re


def test():
    try:
        with open(text, "w") as f:
            f.write(frequency)

    except PermissionError :
        print(f'Permission error ocurred! Unable to read the FILE: {frequency}')



