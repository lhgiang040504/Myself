SOHO : small office / home office

one maindevice = router = WAP = switch

Four weak areas :
    + Straight from the internet

    + Devices that connected to your network (The scariest weak point)
    
    + Your wireless 

    + The connection to your company, your job (The most impactful)

public IP address

2 way to scan our network:
+ pentest-tools, ...
    light scan : it doesn't give you access to the full features
+ nmap


open ports : the port of our firewall that outside device can get into our network, may be we have a website inside our network.



secure:
1. turn on firewall
2. close open_ports (port forwarding)
3. disable remote management (biggest one)
4. change your defaults username and password
5. upgrade firmware, software because the producer found new feature, found a vulnerability with thier hardware and software
6. password wifi, my main network and gues network
7. turn off ping, fly under the radar

(*use device isolation)

port_key : phones, tabets,  laptops, VLAN7, NAS (network attached storage) - pretty trust

seekeroftruth : VLAN6, smart light bulbs

horcruxes : VLAN8, really rellly dont trust : cheap IoT

DD-WRT
custom network on equipment
ubiquiti (prosumer option)


IDS : devices are trying to reach out to - fix it
IPS : where it going - detect it

connect with company
1. remote-access vpn
2. a firewall

home router have already had a vpn