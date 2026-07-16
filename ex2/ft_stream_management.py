import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print("Accessing file '" + sys.argv[1] + "'")
        try:
            file: typing.IO = open(sys.argv[1])
            content = file.read()
            file.close()
            print("---")
            print(content, end="")
            print("---")
            print("File '" + sys.argv[1] + "' closed.")
            print("Transform data:")
            print("---")
            lines = content.split('\n')
            new_lines = []
            for line in lines:
                if line != '':
                    new_lines.append(line + '#')
            new_content = '\n'.join(new_lines)
            print(new_content)
            print("---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new_fragment = sys.stdin.readline().strip('\n')
            if new_fragment == '':
                print("Not saving data.")
            else:
                print("Saving data to '" + new_fragment + "'")
                try:
                    out_file: typing.IO = open(new_fragment, 'w')
                    out_file.write(new_content)
                    out_file.close()
                    print("Data saved in file '" + new_fragment + "'.")
                except OSError as e:
                    sys.stderr.write(
                        "[STDERR] Error opening file '"
                        + new_fragment + "': " + str(e) + "\n"
                    )
                    print("Data not saved.")
        except OSError as e:
            sys.stderr.write(
                "[STDERR] Error opening file '"
                + sys.argv[1] + "': " + str(e) + "\n"
            )
