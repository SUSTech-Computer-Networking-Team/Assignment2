import argparse
import sys

from models import *
from time import sleep
from sockets import *

PING_COUNT = 3  #the number of ICMP echo packet tobe sent whose initial TTL value are same  
PING_INTERVAL = 0.05
PING_TIMEOUT = 2
MAX_HOP = 30


def tracert(address, id=None):
    if is_hostname(address):
        address = resolve(address)[0]

    sock = ICMPSocket()

    id = id or unique_identifier()
    payload = random_byte_message(56)
    ttl = 1
    host_reached = False
    hops = []

    while not host_reached and ttl <= MAX_HOP:
        reply = None
        packets_sent = 0
        rtts = []

        ###############################
        # TODO:
        # Create ICMPRequest and send through socket,
        # then receive and parse reply,
        # remember to modify ttl when creating ICMPRequest
        #
        #
        # :type id: int
        # :param id: The identifier of ICMP Request
        #
        # :rtype: Host[]
        # :returns: ping result
        #
        # Hint: use ICMPSocket.send() to send packet and use ICMPSocket.receive() to receive
        #
        ################################

        # sock._set_ttl(ttl)
        request = ICMPRequest(address, id, 0, ttl=ttl)
        for i in range(PING_COUNT):
            sock.send(request)
            packets_sent += 1

            temp_reply = None
            try:
                temp_reply = sock.receive(request, timeout=PING_TIMEOUT)
            except TimeoutExceeded:
                print(f"time out at TTL {ttl}")
                continue

            if temp_reply:
                rtts.append((temp_reply.time - request.time) * 1000)
                reply = temp_reply
                if reply.source == address:
                    host_reached = True

        # analyze the address of each hop from the received message?

        if reply:
            hop = Hop(
                address=reply.source,
                packets_sent=packets_sent,
                rtts=rtts,
                distance=ttl)

            hops.append(hop)

        ttl += 1
        sleep(PING_INTERVAL)

    return hops


if __name__ == "__main__":
    target = sys.argv[1]
    parser = argparse.ArgumentParser(description="tracert")
    parser.add_argument('--i', type=int, default=None) #指定id值
    args = parser.parse_args(sys.argv[2:])
    hops = tracert(target,args.i)
    for hop in hops:
        print(hop.__str__())
