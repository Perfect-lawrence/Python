#!/usr/bin/env python
# -*- coding:utf8 -*-

import uuid
def get_mac_address():
    local_mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([local_mac[e:e+2] for e in range(0,11,2)])
mac = get_mac_address()
print("mac: %s" % mac)

