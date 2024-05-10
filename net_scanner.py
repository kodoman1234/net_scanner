import scapy.all as scapy
import optparse
import re
#1)request
#2)broadcast
#3)response
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-r","--request",dest="request",help="set to request ip address range!!!")

    (user_inputs, arguments) = parse_object.parse_args()
    if not user_inputs.request:
        print("Enter IP Address!!!")
    return user_inputs
def packet(user_request):
    arp_request_packet = scapy.ARP(pdst=f"{user_request}")
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    return combined_packet

user_ip_address = get_user_input()
(answered,unanswered) = scapy.srp(packet(user_ip_address.request),timeout=1)
answered.summary()






