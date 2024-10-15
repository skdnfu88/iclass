from telethon.sync import TelegramClient, events
import re
import os

# Configuration for the first client
api_id_1 = '28686154'
api_hash_1 = '6e1952e5134002f0b93e5f6a952c1e8d'
your_session_1 = 'akunpratama'

# Configuration for the second client
api_id_2 = '28686153'
api_hash_2 = '6e1952e5134002f0b93e5f6a952c1e8t'
your_session_2 = 'farr'

api_id_3 = '28686153'
api_hash_3 = '6e1952e5134002f0b93e5f6a952c1e8t'
your_session_3 = 'farr'

# ANSI escape codes for colors
RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{RED}Session{RESET}")
    print(f"{GREEN}BY{RESET} {YELLOW}AVAYONA{RESET}")
    print(f"{YELLOW}HARI HARI JEPE{RESET}")
    print("=" * 50)

def start_client(client, client_number):
    @client.on(events.NewMessage)
    async def handle_incoming_message(event):
        otp = re.search(r'\b\d{5}\b', event.raw_text)
        if otp:
            print(f"{GREEN}[*] Your login code from client {client_number}: {otp.group(0)}{RESET}")
            print(f"{RED}Press Ctrl C Untuk Kembali.{RESET}")
    print(f"{YELLOW}Listening for messages on client {client_number}...{RESET}")
    
    with client:
        client.run_until_disconnected()

def main_menu():
    while True:
        print_header()
        print(f"{YELLOW}\nSelect the client you want to run:{RESET}")
        print(f"1. Client 1 ({your_session_1})")
        print(f"2. Client 2 ({your_session_2})")
        print(f"3. Client 3 ({your_session_3})")
        print("666. Exit")

        choice = input(f"\nEnter 1, 2, 3 or 4: {RESET}")

        if choice == '1':
            client1 = TelegramClient(your_session_1, api_id_1, api_hash_1)
            start_client(client1, 1)
        elif choice == '2':
            client2 = TelegramClient(your_session_2, api_id_2, api_hash_2)
            start_client(client2, 2)
        elif choice == '3':
            client3 = TelegramClient(your_session_3, api_id_3, api_hash_3)
            start_client(client3, 3)
        elif choice == '666':
            print(f"{RED}Exiting the program.{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please enter 1, 2, 3 or 4.{RESET}")
        
        # Option to return to the main menu
        back = input(f"{YELLOW}Press Enter to return to the main menu...{RESET}")
        if back == "":
            continue
        else:
            print(f"{RED}Invalid input. Returning to the main menu.{RESET}")
            continue

if __name__ == "__main__":
    main_menu()
