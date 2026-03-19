def vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    try:
        with open("vault_data.txt", "r") as f:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols")

            content = f.read()

            print("SECURE EXTRACTION:")
            print(content)

        with open("secure_protocols.txt", "w") as f:
            print("SECURE PRESERVATION:")

            entry = "[CLASSIFIED] New security protocols archived"
            f.write(entry + "\n")

            print(entry)
        print("All vault operations completed with maximum security.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

    except OSError as e:
        print("Error:", e)


if __name__ == "__main__":
    vault_security()