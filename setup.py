from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
import time

# Setup a basic network with two hosts s and r
# Both hosts are connected to a switch s0
net = Mininet()
c0 = net.addController()
s = net.addHost('s')
r = net.addHost('r')

s0 = net.addSwitch('s0')

net.addLink(s, s0)
net.addLink(r, s0)

# Start the network
net.start()
s.setIP('192.168.1.1', 24)
r.setIP('192.168.1.2', 24)
net.pingAll()

# Run s.py on the host s
s.cmd('python3 s.py > out.txt &')
time.sleep(5)
result = r.cmd('python3 client.py')
print(result)

net.stop()