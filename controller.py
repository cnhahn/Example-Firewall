# Final Skeleton
#
# Hints/Reminders from Lab 4:
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. The following modifications have 
    # been made from Lab 4:
    #   - port_on_switch represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    print "Start!--------------------------------------"

    msg = of.ofp_flow_mod()
    msg.idle_timeout = 40
    msg.hard_timeout = 55
    #ipv4 = packet.find('ipv4')
    #src_ip = ipv4.srcip
    #dst_ip = ipv4.dstip

    ICMP = packet.find('icmp')
    

    if ICMP is not None:
      print "ICMP is not none"
      ipv4 = packet.find('ipv4')
      src_ip = ipv4.srcip
      dst_ip = ipv4.dstip
      msg.match = of.ofp_match.from_packet(packet)

      if switch_id == 1:
        print "switch id = 1st Floor Switch"
        
        if dst_ip == "10.0.1.10":
          print "dst_ip = 10.0.1.10 - host 10"
          action = of.ofp_action_output(port = 1)
        
        else:
          print "src_ip = 10.0.1.10 - host 10"
          action = of.ofp_action_output(port = 5)
          
        msg.match.nw_proto = 1
        msg.data = packet_in
        msg.actions.append(action)
        self.connection.send(msg)

      elif switch_id == 2:
        print "switch id = 2nd Floor Switch"
        msg.match = of.ofp_match.from_packet(packet)

        if dst_ip == "10.0.2.20":
          print "dst ip = 10.0.2.20 - host 20"
          action = of.ofp_action_output(port = 2)
        
        else: 
          print "src ip = 10.0.2.20 - host 20"
          action = of.ofp_action_output(port = 5)
        msg.match.nw_proto = 1
        msg.data = packet_in
        msg.actions.append(action)
        self.connection.send(msg)

      elif switch_id == 3:
        print "switch id = 3rd Floor Switch"
        msg.match = of.ofp_match.from_packet(packet)

        if dst_ip == "10.0.3.30":
         print "dst_ip = 10.0.3.30 - host 30"
         action = of.ofp_action_output(port = 3)
        
        else:
          print "src_ip = 10.0.3.30 - host 30"
          action = of.ofp_action_output(port = 5)
        
        msg.match.nw_proto = 1
        msg.data = packet_in
        msg.actions.append(action)
        self.connection.send(msg)

      elif switch_id == 4:
        print "switch_id = Data Center Switch"

        msg.match = of.ofp_match.from_packet(packet)
        
        if dst_ip == "10.0.4.10":
          print "dst_ip = 10.0.4.10 - server"
          action = of.ofp_action_output(port = 4)
        
        else:
          print "src_ip = 10.0.4.10 - server"
          action = of.ofp_action_output(port = 5)

        msg.match.nw_proto = 1
        msg.data = packet_in
        msg.actions.append(action)
        self.connection.send(msg)

      elif switch_id == 5 and src_ip == "156.134.2.12": 

        print "switch id = core switch and untrusted host"
        
        if dst_ip == "104.82.214.112":
          msg.match = of.ofp_match.from_packet(packet)
          action = of.ofp_action_output(port = 5)
          msg.data = packet_in
          msg.actions.append(action)
        #else:
          #msg.match = of.ofp_match.from_packet(packet)
          #action = of.ofp_action_output(port = of.OFPP_NONE)
          #msg.data = packet_in
          #msg.actions.append(action)
        
        #msg.actions.append(action)
        self.connection.send(msg)
      
      elif switch_id == 5 and src_ip == "104.82.214.112" and dst_ip == "156.134.2.12":

        msg.match = of.ofp_match.from_packet(packet)
        action = of.ofp_action_output(port = 6)
        msg.match.nw_proto = 1
        msg.data = packet_in
        msg.actions.append(action)
        self.connection.send(msg)

      else:
        print "switch id = Core Switch"
        msg.match = of.ofp_match.from_packet(packet)

        if dst_ip == "10.0.1.10":
          print "dst ip = host 10"
          action = of.ofp_action_output(port = 7)
        
        elif dst_ip == "10.0.2.20":
          print "dst ip = host 20"
          action = of.ofp_action_output(port = 8)

        elif dst_ip == "10.0.3.30":
          print "dst ip = host 30"
          action = of.ofp_action_output(port = 9)

        elif dst_ip == "10.0.4.10":
          print "dst ip = server"
          action = of.ofp_action_output(port = 10)

        elif dst_ip == "104.82.214.112":
          print "dst ip = trust host"
          action = of.ofp_action_output(port = 5)

        elif dst_ip == "156.134.2.12":
          print "dst ip = untrust host"
          action = of.ofp_action_output(port = 6) 
      
        else:
          print "error!"

        msg.match.nw_proto = 1
        msg.data = packet_in
        msg.actions.append(action)
        self.connection.send(msg)
      
    else:
      print "ICMP is none"
      ARP = packet.find('arp')
    
      if ARP is not None:
        print "ARP is not none"   
        msg.match = of.ofp_match.from_packet(packet)
        msg.match.dl_type = 0x0806
        action_ARP = of.ofp_action_output(port = of.OFPP_FLOOD)
        msg.actions.append(action_ARP)
        msg.data = packet_in
        self.connection.send(msg)
      
      else:
        print "ARP is none"
        msg.data = packet_in
        
        TCP = packet.find('tcp')

        ipv4 = packet.find('ipv4')
        src_ip = ipv4.srcip
        dst_ip = ipv4.dstip
        msg.match = of.ofp_match.from_packet(packet)

        if TCP is not None:
          print"TCP is not none"

          if switch_id == 5 and  src_ip == "156.134.2.12" and dst_ip == "104.82.214.112": 
            print "src = untrusted host -> dst = trusted host" 
            #msg.match = of.ofp_match.from_packet(packet)
            msg.match.nw_proto = 6
            action = of.ofp_action_output(port = 5)
            msg.actions.append(action)
            msg.data = packet_in
            self.connection.send(msg)

          elif  switch_id == 5 and src_ip == "104.82.214.112" and dst_ip == "156.134.2.12":
            print "src = trusted host -> dst = untrusted host"
            #msg.match = of.ofp_match.from_packet(packet)
            msg.match.nw_proto = 6
            action = of.ofp_action_output(port = 6)
            msg.actions.append(action)
            msg.data = packet_in
            self.connection.send(msg)

          elif switch_id == 5 and src_ip == "156.134.2.12" and dst_ip == "10.0.4.10":
            print "src = untrusted host -> dst = server"
            self.connection.send(msg)

          elif switch_id == 5 and src_ip == "10.0.4.10" and dst_ip == "156.134.2.12":
            print "src = server -> dst = untrusted host"
            self.connection.send(msg)

          #elif switch_id == 5 and src_ip == "156.134.2.12":
            #print "src = untrusted host"

            #action = of.of_action_output(port = of.OFPP_NONE)
            #msg.actions.append(action)
            #msg.data = packet_in
            #self.connection.send(msg)

          #elif switch_id == 5 and dst_ip == "156.134.2.12":
            #print "dst = untrsuted host"
            
            #action = of.of_action_output(port = of.OFPP_NONE)
            #msg.actions.append(action)
            #msg.data = packet_in
            #self.connection.send(msg)
          
          elif switch_id == 1:
            print "TCP : switch id = 1 - 1st floor switch"
          
            if dst_ip == "10.0.1.10":
              print "dst_ip = 10.0.1.10 - host 10"
              action = of.ofp_action_output(port = 1)
            
            else:
              print "src_ip = 10.0.1.10 - host 10"
              action = of.ofp_action_output(port = 5)
              
            msg.match.nw_proto = 6
            msg.data = packet_in
            msg.actions.append(action)
            self.connection.send(msg)

          elif switch_id == 2:
            print "TCP : switch id = 2 - 2nd floor switch"
            
            if dst_ip == "10.0.2.20":
              print "dst ip = 10.0.2.20 - host 20"
              action = of.ofp_action_output(port = 2)
            
            else:
              print "src ip = 10.0.2.20 - host 20"
              action = of.ofp_action_output(port = 5)
            
            msg.match.nw_proto = 6
            msg.data = packet_in
            msg.actions.append(action)
            self.connection.send(msg)
            
          elif switch_id == 3:
            print "TCP : switch id = 3 - 3rd floor switch"

            if dst_ip == "10.0.3.30":
              print "dst ip = 10.0.3.30 - host 30"
              action = of.ofp_action_output(port = 3)
            
            else:
              print "src ip = 10.0.3.30 - host 30"
              action = of.ofp_action_output(port = 5)
            
            msg.match.nw_proto = 6
            msg.data = packet_in
            msg.actions.append(action)
            self.connection.send(msg)

          elif switch_id == 4:
            print "TCP : switch id = 4 - 4th floor switch"
            
            if dst_ip == "10.0.4.10":
              print "dst ip = 10.0.4.10 - server"
              action = of.ofp_action_output(port = 4)
            
            else:
              print "src ip = 10.0.4.10 - server"
              action = of.ofp_action_output(port = 5)
            
            msg.match.nw_proto = 6
            msg.data = packet_in
            msg.actions.append(action)
            self.connection.send(msg)

          elif switch_id == 5:
            print "TCP : switch id = 5 - core switch"
            
            if dst_ip == "10.0.1.10":
              print "dst ip = host 10"
              action = of.ofp_action_output(port = 7)
            
            elif dst_ip == "10.0.2.20":
              print "dst ip = host 20"
              action = of.ofp_action_output(port = 8)
            
            elif dst_ip == "10.0.3.30":
              print "dst ip = host 30"
              action = of.ofp_action_output(port = 9)
            
            elif dst_ip == "10.0.4.10":
              print "dst ip = server"
              action = of.ofp_action_output(port = 10)
            
            elif dst_ip == "104.82.214.112":
              print "dst ip = trusted host"
              action = of.ofp_action_output(port = 5)
            
            elif dst_ip == "156.134.2.12":
              print "dst_ip = untrusted host"
              action = of.ofp_action_output(port = 6)
            
            else:
              print "error!"
          
            msg.match.nw_proto = 6
            msg.data = packet_in
            msg.actions.append(action)
            self.connection.send(msg)

        else:
          
          print "TCP is none"
          msg.data = packet_in

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
