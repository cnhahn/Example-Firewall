#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):
    
    # Examples!
    # Create a host with a default route of the ethernet interface. You'll need to set the
    # default gateway like this for every host you make on this assignment to make sure all 
    # packets are sent out that port. Make sure to change the h# in the defaultRoute area
    # and the MAC address when you add more hosts!
    #h1 = self.addHost('h1',mac='00:00:00:00:00:01',ip='1.1.1.1/24', defaultRoute="h1-eth0")
    #h2 = self.addHost('h2',mac='00:00:00:00:00:02',ip='2.2.2.2/24', defaultRoute="h2-eth0")

    # Create a switch. No changes here from Lab 1.
    #s1 = self.addSwitch('s1')

    # Connect Port 8 on the Switch to Port 0 on Host 1 and Port 9 on the Switch to Port 0 on 
    # Host 2. This is representing the physical port on the switch or host that you are 
    # connecting to.
    #self.addLink(s1,h1, port1=8, port2=0)
    #self.addLink(s1,h2, port1=9, port2=0)
    

###############################################################################


    #hosts 10, 20, 30
    h10 = self.addHost('h10', mac='00:00:00:00:00:10', ip='10.0.1.10/24', defaultRoute="h10-eth0")
    h20 = self.addHost('h20', mac='00:00:00:00:00:20', ip='10.0.2.20/24', defaultRoute="h20-eth0")
    h30 = self.addHost('h30', mac='00:00:00:00:00:30', ip='10.0.3.30/24', defaultRoute="h30-eth0")
    

    #floor switchs 1, 2, 3
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')

    #linking the proper host to the proper floor switch as described in the lab
    self.addLink(s1,h10, port1=1, port2=0)
    self.addLink(s2,h20, port1=2, port2=0)
    self.addLink(s3,h30, port1=3, port2=0)
    #self.addLink(s1,h10, port1=1, port2=1)
    #self.addLink(s2,h20, port1=1, port2=1)
    #self.addLink(s3,h30, port1=1, port2=1)

    #host server
    h4 = self.addHost('h4', mac='00:00:00:00:00:40', ip='10.0.4.10/24', defaultRoute="h4-eth0")

    #data center switch
    s4 = self.addSwitch('s4')
    
    #linking the data center switch with the sever
    self.addLink(s4, h4, port1=4, port2=0)
    #self.addLink(s4, server)

    #trusted host and untrusted host
    h5 = self.addHost('h5', mac='00:00:00:00:00:50', ip='104.82.214.112/24', defaultRoute="h5-eth0")
    h6 = self.addHost('h6', mac='00:00:00:00:00:51', ip='156.134.2.12/24', defaultRoute="h6-eth0")
    
    #core switch
    s5 = self.addSwitch('s5')

    self.addLink(s5,h5, port1=5, port2=0)
    #self.addLink(s5, th)
    
    self.addLink(s5,h6, port1=6, port2=0)
    #self.addLink(s5,uth)

    #core switch - f1s
    self.addLink(s5,s1, port1=7, port2=5)
    #self.addLink(s5,s1)

    #core switch - f2s
    self.addLink(s5,s2, port1=8, port2=5)
    #self.addLink(s5,s2)

    #core switch - f3s
    self.addLink(s5,s3, port1=9, port2=5)
    #self.addLink(s5,s3)
    
    #core switch - data center switch
    self.addLink(s5,s4, port1=10, port2=5)
    #self.addLink(s5, s4)


def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
