import argparse
import requests
import time

GREEN = '\033[92m'
RED = '\033[91m'
# rpm = request per second

def directory_buster(url, wordlist, rps):
    try:
        with open(wordlist, 'r') as f:
            for line in f:
                directory = line.strip()
                target_url = url + '/' + directory
                response = requests.get(target_url)
                if response.status_code == 200:
                    print(GREEN + str(response.status_code) + ' [+] Discovered directory:', target_url)
                else:
                    print(RED + str(response.status_code) +' [+] Directory not found: ', target_url)
                if(rps):
                    time.sleep(1/rps)
    except FileNotFoundError:
        print('Wordlist file not found.')


if __name__ == "__main__":
    ascii_art = r"""
________  .__      ___.                   __   
\______ \ |__|_____\_ |__  __ __  _______/  |_ 
 |    |  \|  \_  __ \ __ \|  |  \/  ___/\   __\
 |    `   \  ||  | \/ \_\ \  |  /\___ \  |  |  
/_______  /__||__|  |___  /____//____  > |__|  
        \/              \/           \/         
    """
    print(ascii_art)
    parser = argparse.ArgumentParser(description='Simple directory buster tool.')
    parser.add_argument('-u', '--url', type=str, help='Target URL', required=True)
    parser.add_argument('-w', '--wordlist', type=str, help='Path to the wordlist', required=True)
    parser.add_argument('-r', '--request_per_second', type=int, help='No of Request per second', required=False, default=5.0)

    args = parser.parse_args()
    directory_buster(args.url, args.wordlist, args.request_per_second)
