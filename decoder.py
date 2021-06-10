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
    print("[*] Warning: NOT allowed to have space")
    hex_string = input("[*] Enter your code: ")
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")

    print("[*] Processing...")
    time.sleep(3)

    print(f'[*] Decoded: {ascii_string}')

elif choice == 2:
    print("[*] Warning: NOT allowed to have space")
    binary_string = input("[*] Enter your code: ")

    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    print("[*] Processing...")
    time.sleep(3)

    print(f'[*] Decoded {hexadecimal_string}')

elif choice == 3:
    print("[*] Warning: It is necessary to have spaces")
    a_binary_string = input("[*] Enter your code: ")

    binary_values = a_binary_string.split()

    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character

    print("[*] Processing...")
    time.sleep(3)
    print(f'[*] Decoded: {ascii_string}')

else:
    print("Try again.")

# Admin password for 652.534.765
# R329321
