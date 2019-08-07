#!/usr/bin/env python3
import uuid
def get_mac_address():
    mac=uuid.uuid1().hex[-12:]
    return "-".join([mac[e:e+2] for e in range(0,11,2)])


if __name__=="__main__":
    print(get_mac_address())
