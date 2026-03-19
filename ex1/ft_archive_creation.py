def write_in_file() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")

    try:
        with open("new_discovery.txt", "w") as f:
            print("Storage unit created successfully..")
            print("Inscribing preservation data...")
            entry1 = "[ENTRY 001] New quantum algorithm discovered"
            entry2 = "[ENTRY 002] Efficiency increased by 347%"
            entry3 = "[ENTRY 003] Archived by Data Archivist trainee"

            f.write(entry1 + "\n")
            f.write(entry2 + "\n")
            f.write(entry3 + "\n")

            print(entry1)
            print(entry2)
            print(entry3)
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

    except OSError as e:
        print("Error:", e)


if __name__ == "__main__":
    write_in_file()
