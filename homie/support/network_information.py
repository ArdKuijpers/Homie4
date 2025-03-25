#!/usr/bin/env python

import logging
import netifaces
import socket
import uuid

logger = logging.getLogger(__name__)

class Network_Information(object):
    """Util for getting a interface' ip to a specific host and the corresponding mac address."""

    # def __init__(self):
    #     self.ip_to_interface = self.__build_ip_to_interface_dict()

    # def __build_ip_to_interface_dict(self):
    #     """Build a map of IPv4-Address to Interface-Name (like 'eth0')"""
    #     map = {}
    #     for interface in netifaces.interfaces():
    #         try:
    #             ifInfo = netifaces.ifaddresses(interface)[netifaces.AF_INET]
    #             for addrInfo in ifInfo:
    #                 addr = addrInfo.get("addr")
    #                 if addr:
    #                     map[addr] = interface
    #         except Exception:
    #             pass
    #     return map

    def get_local_ip(self, targetHost, targetPort):
        """Gets the local ip to reach the given ip.
        That can be influenced by the system's routing table.
        A socket is opened and closed immediately to achieve that."""
        ip = "NoIP"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((targetHost, targetPort))
        except Exception as e:
            logger.exception(
                "Cannot create socket to target " + targetHost + ":" + targetPort
            )
        else:
            ip = s.getsockname()[0]
            s.close()
        return ip

    def get_local_mac(self):
        _mac = '{:02x}'.format(uuid.getnode())
        mac_addr = ':'.join([_mac[i:i+2]for i in range(0,12,2)])
        return mac_addr
