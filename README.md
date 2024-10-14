DEAUTH.WIFI
==========

A Scapy script for deauthing and manipulating WiFi networks.

**WARNING**

This script is for educational and testing purposes only. Using it to deauth or DDOS WiFi networks without permission is illegal and unethical. I am not responsible for any misuse or damage caused by this script.

**USAGE**

Install the script using `pip install .` in the repository directory.

Run the script using the `deauth.wifi` command, followed by the desired options and arguments.

**OPTIONS**

* `-i` or `--interface`: Wireless interface to use (required)
* `-b` or `--bssid`: BSSID of the WiFi network to target
* `-c` or `--count`: Number of packets to send (default: 1 for deauth, 100 for DDOS)
* `-d` or `--deauth`: Deauth the WiFi network
* `-D` or `--ddos`: DDOS the WiFi network

**EXAMPLE**

This will deauth the WiFi network with the specified BSSID using the `wlan0` interface.

**DISCLAIMER**

I am not responsible for any misuse or damage caused by this script. Use at your own risk.
