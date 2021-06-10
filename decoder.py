import time


logo = """
 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀  ██████  ██░ ██  ██▓▓█████  ██▓    ▓█████▄
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▒██    ▒ ▓██░ ██▒▓██▒▓█   ▀ ▓██▒    ▒██▀ ██▌
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ░ ▓██▄   ▒██▀▀██░▒██▒▒███   ▒██░    ░██   █▌
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄   ▒   ██▒░▓█ ░██ ░██░▒▓█  ▄ ▒██░    ░▓█▄   ▌
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒██████▒▒░▓█▒░██▓░██░░▒████▒░██████▒░▒████▓
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░░ ▒░ ░░ ▒░▓  ░ ▒▒▓  ▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░ ░ ░  ░░ ░ ▒  ░ ░ ▒  ▒
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ ░  ░  ░   ░  ░░ ░ ▒ ░   ░     ░ ░    ░ ░  ░
 ░  ░  ░      ░  ░░ ░      ░  ░         ░   ░  ░  ░ ░     ░  ░    ░  ░   ░
                  ░                                                    ░
"""
print('\033[32m'+logo+'\033[32m')
print("1. Hex to Text\n2. Binary to Hex\n3. Binary to Text")
choice = int(input("\n[*] Enter your choice: "))
if choice == 1:
    hex_string = input("[*] Enter your code: ")
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")

    print("[*] Processing...")
    time.sleep(3)

    print(f'[*] Decoded: {ascii_string}')

elif choice == 2:
    binary_string = input("[*] Enter your code: ")

    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    print("[*] Processing...")
    time.sleep(3)

    print(f'[*] Decoded {hexadecimal_string}')

else:
    print("Try again.")
