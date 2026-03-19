def read_file() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        f = open("ancient_fragment.txt", "r")
        content = f.read()
        f.close()

        print("Connection established...")
        print("RECOVERED DATA:")
        print(content)
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    read_file()
