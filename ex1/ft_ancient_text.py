import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print("Accessing file '" + sys.argv[1] + "'")
        try:
            file: typing.IO = open(sys.argv[1])
            content = file.read()
            file.close()
            print("---\n")
            print(content, end="\n")
            print("---")
            print("File '" + sys.argv[1] + "' closed.")
        except OSError as e:
            print("Error opening file '" + sys.argv[1] + "': " + str(e))
