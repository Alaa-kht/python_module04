*This project has been created as part of the 42 curriculum by aalkhati.*

# Data Archivist - Digital Preservation in the Cyber Archives

> "Your tools are simple but powerful: the ability to open data vaults, read their contents, write new archives, and handle the unexpected without losing precious information."

This project is a port of 42 school's Data Archivist project, focused on mastering file operations, managing data streams, and building robust archival systems.

---

## About

Preserve digital knowledge by mastering file operations, managing data streams, and building robust archival systems that protect information.

---

## Requirements

- Python 3.10 or later
- Code must comply with `flake8` linter standards
- All functions must include type hints (checked with `mypy`)
- Exceptions must be handled gracefully to avoid crashes
- **Note:** The `with` statement is only introduced in Exercise 3 — do not use it before then

---

## Important Note for Windows Users

The permission denied test (`[Errno 13]`) cannot be fully tested using `chmod 000` on Windows as it does not enforce Unix-style file permissions. To test permission denied errors on Windows use a protected system file instead:

```bash
python ft_ancient_text.py C:/Windows/System32/config/SAM
```

This will correctly trigger the `[Errno 13] Permission denied` error. The code handles it correctly regardless of OS.

---

## Usage

```bash
python ft_ancient_text.py ancient_fragment.txt
python ft_archive_creation.py ancient_fragment.txt
python ft_stream_management.py ancient_fragment.txt
python ft_vault_security.py
```

To create the test file used in exercises 0, 1, and 2:

```bash
cat > ancient_fragment.txt << 'EOF'
[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion
EOF
```

---

## Exercises

---

### Exercise 0 - Ancient Text Recovery (`ex0/ft_ancient_text.py`)

**Description:**
Read a file passed as a command-line argument and display its contents like the `cat` command, with headers and footers. Handle all failure cases gracefully.

**Instructions:**
- Get filename from `sys.argv`
- Print usage message if no argument provided
- Open the file using `open()` and read with `.read()`
- Display content between `---` separators
- Close the file with `.close()`
- Handle file not found and permission denied errors with `OSError`

**Concepts:** `open()`, `.read()`, `.close()`, `typing.IO`, `OSError`, `try/except`

---

### Exercise 1 - Archive Creation (`ex1/ft_archive_creation.py`)

**Description:**
Build on Exercise 0 — after reading the file, transform the content by adding `#` at the end of each line, then optionally save it to a new file.

**Instructions:**
- Read the file exactly as in Exercise 0
- Split content into lines and append `#` to each non-empty line
- Display the transformed content between `---` separators
- Ask user for a new filename using `input()`
- If filename provided, open in write mode `'w'` and save
- If empty, print "Not saving data."
- Handle write errors with `OSError`

**Concepts:** `str.split()`, `str.join()`, `open()` write mode `'w'`, `.write()`, `input()`

---

### Exercise 2 - Stream Management (`ex2/ft_stream_management.py`)

**Description:**
Build on Exercise 1 — redirect all error messages to `sys.stderr` and replace `input()` with `sys.stdin.readline()`.

**Instructions:**
- Same logic as Exercise 1
- Replace all error `print()` calls with `sys.stderr.write()` and add `[STDERR]` prefix
- Replace `input()` with `sys.stdout.write()` + `sys.stdout.flush()` + `sys.stdin.readline().strip('\n')`
- On write failure print "Data not saved."

**Concepts:** `sys.stdin`, `sys.stdout`, `sys.stderr`, `io.readline()`, `io.flush()`, `io.write()`

---

### Exercise 3 - Vault Security (`ex3/ft_vault_security.py`)

**Description:**
Use the `with` statement (context manager) to ensure safe and automatic file handling. Implement a `secure_archive()` function that reads or writes files and returns a result tuple.

**Instructions:**
- Write `secure_archive(filename, action, content)` function
- Use `with open(...) as f:` for all file operations
- Returns `(True, content)` on success
- Returns `(False, error_message)` on failure
- Test with nonexistent file, inaccessible file, valid read, and valid write

**Concepts:** `with` statement, context manager, `tuple` return values, optional parameters

**Why `with` is better:**
```python
# without with — file may never close if error occurs
file = open("file.txt")
content = file.read()
file.close()  # never reached if read() crashes!

# with with — always closes automatically
with open("file.txt") as f:
    content = f.read()
# closed here no matter what
```

---

## Key Concepts Summary

| Concept | Description |
|---------|-------------|
| `open(file, 'r')` | Open file for reading (default) |
| `open(file, 'w')` | Open file for writing, creates or replaces |
| `.read()` | Read entire file as one string |
| `.write(str)` | Write string to file |
| `.close()` | Close file manually |
| `with open() as f` | Auto-closes file even if error occurs |
| `sys.stdin` | Read input from keyboard |
| `sys.stdout` | Normal output stream |
| `sys.stderr` | Error output stream |
| `OSError` | Catches file not found and permission denied |
