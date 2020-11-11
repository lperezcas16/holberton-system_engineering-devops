# 0x08. Networking basics #1
<div align="center"><img src="images/local.png" width=250/>
</div>

## Resources:books:
Read or watch:
* [What is localhost](https://intranet.hbtn.io/rltoken/7SedZ8ILSQulYf7xzSbraQ)
* [What is 0.0.0.0](https://intranet.hbtn.io/rltoken/n5IFAt_OWGJtGW33t7Jfag)
* [What is the hosts file](https://intranet.hbtn.io/rltoken/21l3Uqizr3LpA1ZGrYPg3g)
* [Netcat examples](https://intranet.hbtn.io/rltoken/uMleIIzkRoR2w8EkwItSEg)

---
## Learning Objectives:bulb:
What you should learn from this project:

### What is localhost/127.0.0.1
* The IP address 127.0.0.1 is a special-purpose IPv4 address and is called the localhost or loopback address. All computers use this address as their own, but it doesn't let computers communicate with other devices as a real IP address does. 127.0.0.1 has one specific purpose of allowing a device to send messages to itself. You can also call it a **loopback network interface**. See more --> [LifeWire](https://www.lifewire.com/network-computer-special-ip-address-818385)
### What is 0.0.0.0
* This IP address is structured like a regular one (it has four places for numbers). However, it's a placeholder address or one that's used to describe that there isn't a normal address assigned—neither public nor private. For example, instead of putting no IP address into the network area of a program, 0.0.0.0 can be used to mean anything from accept all IP addresses or block all IP addresses to the default route. See more --> [LifeWire](https://www.lifewire.com/four-zero-ip-address-818384)
### What is /etc/hosts
* The Hosts file (also referred to as etc/hosts) is a text file used to map IP addresses to host names or domain names. This file acts as a local DNS service, for your local computer, and it overrides the mappings from the DNS server that your computer is connected to, through the network.
### How to display your machine’s active network interfaces
*  The “netstat,” or network statistics, is a command-line tool that can be used to uncover problems or detect the amount of traffic in the network. Fortunately, this command can be employed in a few simple steps.
---

### [0. Localhost](./0-localhost)
* What is localhost?


### [1. All IPs](./1-wildcard)
* What is 0.0.0.0?


### [2. Change your home IP](./2-change_your_home_IP)
* Write a Bash script that configures an Ubuntu server with the below requirements.


### [3. Show attached IPs](./3-show_attached_IPs)
* Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.


### [4. Port listening on localhost](./4-port_listening_on_localhost)
* Write a Bash script that listens on port 98 on localhost.

---

## Author
* **Laura Perez** - [lperezcas16](https://github.com/lperezcas16)
