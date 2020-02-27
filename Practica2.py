import os

hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping -c 1 "+hostname)

if respuesta==0:
    print(hostname + ": esta en funcionamiento!")
else:
    print(hostname + ": no funciona!")

red="200.33.171.0/24"
os.system("nmap -sP " + red)

"""PING denebvirtual.itmorelia.edu.mx (200.33.171.77) 56(84) bytes of data.
64 bytes from denebvirtual.itmorelia.edu.mx (200.33.171.77): icmp_seq=1 ttl=56 time=71.6 ms

--- denebvirtual.itmorelia.edu.mx ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 71.629/71.629/71.629/0.000 ms
www.itmorelia.edu.mx: esta en funcionamiento!
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 11:58 CST
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.089s latency).
Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.076s latency).
Nmap scan report for 200.33.171.13
Host is up (0.049s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)
Host is up (0.077s latency).
Nmap scan report for sagitario.itmorelia.edu.mx (200.33.171.65)
Host is up (0.060s latency).
Nmap scan report for 200.33.171.66
Host is up (0.060s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.076s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.073s latency).
Nmap scan report for 200.33.171.85
Host is up (0.093s latency).
Nmap scan report for 200.33.171.97
Host is up (0.10s latency).
Nmap scan report for 200.33.171.98
Host is up (0.10s latency).
Nmap scan report for 200.33.171.99
Host is up (0.10s latency).
Nmap scan report for 200.33.171.115
Host is up (0.080s latency).
Nmap scan report for 200.33.171.118
Host is up (0.085s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.070s latency).
Nmap scan report for 200.33.171.125
Host is up (0.067s latency).
Nmap scan report for 200.33.171.127
Host is up (0.067s latency).
Nmap scan report for 200.33.171.128
Host is up (0.070s latency).
Nmap scan report for 200.33.171.160
Host is up (0.091s latency).
Nmap scan report for 200.33.171.254
Host is up (0.078s latency).
Nmap done: 256 IP addresses (20 hosts up) scanned in 3.20 seconds
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 11:58 CST
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.06 seconds
TCP/IP fingerprinting (for OS scan) requires root privileges.
QUITTING!
paco@Paquito:~$ /bin/python3 /home/paco/Documentos/Practica2.py
PING denebvirtual.itmorelia.edu.mx (200.33.171.77) 56(84) bytes of data.
64 bytes from denebvirtual.itmorelia.edu.mx (200.33.171.77): icmp_seq=1 ttl=56 time=736 ms

--- denebvirtual.itmorelia.edu.mx ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 735.610/735.610/735.610/0.000 ms
www.itmorelia.edu.mx: esta en funcionamiento!
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 11:58 CST
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.11s latency).
Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.067s latency).
Nmap scan report for 200.33.171.13
Host is up (0.074s latency).
Nmap scan report for sagitario.itmorelia.edu.mx (200.33.171.65)
Host is up (0.063s latency).
Nmap scan report for 200.33.171.66
Host is up (0.089s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.089s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.089s latency).
Nmap scan report for 200.33.171.85
Host is up (0.082s latency).
Nmap scan report for 200.33.171.97
Host is up (0.083s latency).
Nmap scan report for 200.33.171.98
Host is up (0.078s latency).
Nmap scan report for 200.33.171.99
Host is up (0.077s latency).
Nmap scan report for 200.33.171.115
Host is up (0.080s latency).
Nmap scan report for 200.33.171.118
Host is up (0.080s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.094s latency).
Nmap scan report for 200.33.171.127
Host is up (0.091s latency).
Nmap scan report for 200.33.171.128
Host is up (0.098s latency).
Nmap scan report for 200.33.171.160
Host is up (0.10s latency).
Nmap scan report for 200.33.171.254
Host is up (0.070s latency).
Nmap done: 256 IP addresses (18 hosts up) scanned in 3.56 seconds"""
