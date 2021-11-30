from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI

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

# Run s.py on the host s
result = s.cmd('python3 s.py')
print(result)

net.stop()