import os
import sys
import requests
from time import sleep

def load_tor():
    os.system("service tor start")

def check_root():
    return os.geteuid() == 0


def reload_tor():
    os.system("service tor reload")

def get_ip(proxy):
    url = "httpps://httpbin.org/ip"
    request = requests.get(url, proxies=proxy)
    return request.json().get('origin')

def create_proxy():
    proxy = {'http':'socks5://127.0.0.1:9050',
              'https':'socks5://127.0.0.1:9050'} 
    return proxy
def main():
    if check_root():
        try:
            change = int(input("After how much time do you want to change your Ip?:"))   
            load_tor()
            current_ip = get_ip(create_proxy())
            print("Your current ip is ::: {}".format(current_ip))
            while True:
                sleep(change)
                reload_tor()
                current_ip = get_ip(create_proxy())
                print("your current IP is ::: {}".format(current_ip))
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()
    else:
        print("Please run with root")
        sys.exit()

if __name__ == "__main__":
    main()