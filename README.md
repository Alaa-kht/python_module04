# Data Archivist – Digital Preservation in the Cyber Archives

> This project has been created as part of the 42 curriculum by aalkhati.

---

## Description

Data Archivist is an introductory Python project from the 42 core curriculum.
Its main goal is to introduce the fundamentals of file I/O and resource management in Python.

Through a set of small, focused exercises, this module covers:

- Reading from and writing to files
- Managing the three standard streams: `stdin`, `stdout`, `stderr`
- Using context managers (`with` statement) for safe resource handling
- Error handling with `try/except` blocks
- Writing clean, typed Python code following 42 standards

Each exercise is isolated in its own directory (`ex0`, `ex1`, etc.) and is designed
to encourage clean, readable, and logical code.

---

## Project Structure

```
data_archivist/
├── ex0/
│   └── ft_ancient_text.py
├── ex1/
│   └── ft_archive_creation.py
├── ex2/
│   └── ft_stream_management.py
├── ex3/
│   └── ft_vault_security.py
├── ex4/
│   └── ft_crisis_response.py
└── README.md
```

---

## What Each Exercise Teaches

| Exercise | File | Concept |
|----------|------|---------|
| Ex0 | `ft_ancient_text.py` | Reading a file with `open()` and `read()` |
| Ex1 | `ft_archive_creation.py` | Writing to a file with `open()` and `write()` |
| Ex2 | `ft_stream_management.py` | Standard streams: `stdin`, `stdout`, `stderr` |
| Ex3 | `ft_vault_security.py` | Context managers with the `with` statement |
| Ex4 | `ft_crisis_response.py` | Error handling with `try/except` |

---

## Requirements

- Python 3.10+
- Code must respect 42 rules:
  - No forbidden functions
  - Correct file and function naming
  - Type hints on all functions
  - No unnecessary files
  - Flake8 compliant

---

## How to Run

First generate the required test files:

```bash
tar -xzf data-generator-tools.tar.gz
python3 data_generator.py
```

Then run each exercise individually from its directory:

```bash
python3 ex0/ft_ancient_text.py
python3 ex1/ft_archive_creation.py
python3 ex2/ft_stream_management.py
python3 ex3/ft_vault_security.py
python3 ex4/ft_crisis_response.py
```

For Ex3, make sure `vault_data.txt` exists before running:

```bash
echo "[CLASSIFIED] Quantum encryption keys recovered
[CLASSIFIED] Archive integrity: 100%" > ex3/vault_data.txt
```

For Ex4, simulate a permission error for `classified_vault.txt`:

```bash
touch ex4/classified_vault.txt
chmod 000 ex4/classified_vault.txt
```

---

## Technical Choices

- **`with` statement** — used over manual `open/close` to guarantee file handles
  are released even when exceptions occur, preventing data corruption and resource leaks.
- **Separate `try` blocks per file** — each file access attempt is independent so
  one failure does not prevent the others from running.
- **Specific exception types** — `FileNotFoundError` and `PermissionError` are caught
  explicitly rather than using a bare `except`, making error handling precise and readable.

---

## Resources

- Python Official Documentation — https://docs.python.org/3/
- PEP 8 – Python Style Guide — https://peps.python.org/pep-0008/
- Python File I/O — https://docs.python.org/3/tutorial/inputoutput.html

---

## AI Usage

> Claude (Anthropic) was used for:
> - Explaining Python file I/O concepts and standard stream behavior
> - Reviewing code structure and pointing out bugs without generating code directly
> - Guiding understanding of `with`, `try/except`, and exception types

---

## Submission Rules

> Only the `exX` directories and this `README.md` must be submitted.
> Any helper files or local testing scripts must not be included.
> File names and function names must strictly follow the subject requirements.

---

## Author

Login: aalkhati
