import os

hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping -c 1 "+hostname)

if respuesta==0:
    print(hostname + ": esta en funcionamiento!")
else:
    print(hostname + ": no funciona!")

red="200.33.171.0/24"
os.system("nmap -sP " + red)

computadora="200.33.171.1"
os.system("nmap -sT " + computadora)

computadora="200.33.171.1"
os.system("nmap -O " + computadora)

"""PING denebvirtual.itmorelia.edu.mx (200.33.171.77) 56(84) bytes of data.
 64 bytes from denebvirtual.itmorelia.edu.mx (200.33.171.77): icmp_seq=1 ttl=56 time=76.2 ms

--- denebvirtual.itmorelia.edu.mx ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 76.171/76.171/76.171/0.000 ms
www.itmorelia.edu.mx: esta en funcionamiento"""

