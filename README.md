![logo](https://i.ibb.co/tqJDc87/pmap-logo-github.png](https://i.ibb.co/2Mf8c9B/68747470733a2f2f692e6962622e636f2f74714a446338372f706d61702d6c6f676f2d6769746875622e706e67-removebg.png))
# PMAP - Python Port Scanner
Welcome to the repository of PMAP!
### What is PMAP?
PMAP is an open source port scanner writen in Python for only educational purposes.
You only need the target's IP address, and a two port number to make it work.
```
[PMAP]> ipsetup>ip> Add the target's IP address: 192.168.1.X
[PMAP]> Validating the IP address...
[PMAP]> Enter the first port: 1
[PMAP]> Enter the last port: 3
```
### How to use it?
As I said, you only need a first and a last port number, then PMAP scans all of them between this two value, and the target's IP address.
If you want to test it on your Global IP address, just visit this site: https://whatismyipaddress.com
### Can I use the Source Code?
Well, if you want to use it, it's may be a sign of not being a skid, so yes, you can. Use the code as you please, but only if you mention the creator's name (nikkeisadev, so me).
### Code example:
```
try:
  for port in range(int(startPort), int(endPort)+1):
      print(Fore.BLUE + "Checking port {} ...".format(port))
      server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      server_sock.settimeout(5)
      result = server_sock.connect_ex((remote_server_ip, port))
      #If the result exit value is equals 0 it's means that it's a hit (an openport)
      if result == 0:
          hits += 1
          print(Fore.GREEN + "======================OPEN=======================" + Fore.BLUE + "")
          print(Fore.GREEN + "", ip, Fore.GREEN + "PORT ==> " + Fore.GREEN + "OPEN".format(port))
      #And, ofc, if it's a bigger value, like 1 bit, it's a nope. So it's a closed port.
      else:
          fails += 1
          print(Fore.RED + "", ip, Fore.RED + "PORT ==> " + Fore.RED + "CLOSED".format(port))
          print(Fore.YELLOW + "Info:" + Fore.YELLOW, errno.errorcode[result])
      server_sock.close()
except socket.error:
    #There is a possibility that the server went down while scanning, so ya can detect it.
    print(Fore.RED + f"{PMAP_PREFIX}The host seems to be down!" + Fore.WHITE +"[" + Fore.RED + "ERR" + Fore.WHITE + "]")
    sys.exit()

```
This is the scanning part of the code. As you noticed, it's using ```sockets``` to scan the address by sending packets.
Also, I really like colored terminal applications, so I choosed to use ```colorama```, it's a Python package too.
You can find ```requirements.txt``` in source folder.
> PMAP is a very basic scanner, also being slow, so it's not recommended for everyday use, it's better for learning how does it works.

# PyInstaller module build support:
I dunno why do anyone wanna build this terminal application, but why not. There is how to make it:
Well, logicaly the build 'ill be a Windows application (.exe), so only Windows supported.
```python -m PyInstaller pmap.py``` for a simple build, but if you want to add icon (.ico) just add ```--icon=iconname.ico``` before pmap.py.
