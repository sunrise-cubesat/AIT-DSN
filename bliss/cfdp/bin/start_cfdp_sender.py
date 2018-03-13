#!/usr/bin/env python

# Advanced Multi-Mission Operations System (AMMOS) Instrument Toolkit (AIT)
# Bespoke Link to Instruments and Small Satellites (BLISS)
#
# Copyright 2017, by the California Institute of Technology. ALL RIGHTS
# RESERVED. United States Government Sponsorship acknowledged. Any
# commercial use must be negotiated with the Office of Technology Transfer
# at the California Institute of Technology.
#
# This software may be subject to U.S. export control laws. By accepting
# this software, the user agrees to comply with all applicable U.S. export
# laws and regulations. User has the responsibility to obtain export licenses,
# or other export authority as may be required before exporting such
# information to foreign countries or providing access to foreign persons.

import bliss.cfdp
import gevent
import traceback

import logging
from bliss.cfdp.primitives import TransmissionMode
from bliss.cfdp import settings

if __name__ == '__main__':

    cfdp = bliss.cfdp.CFDP('1')
    try:
        destination_id = '2'
        source_file = 'test.txt'
        destination_file = 'my/test/blah.txt'
        cfdp.put(destination_id, source_file, destination_file, transmission_mode=TransmissionMode.NO_ACK)
        while True:
            # logging.debug('Sleeping...')
            gevent.sleep(1)
    except KeyboardInterrupt:
        print "Disconnecting..."
    except Exception as e:
        print traceback.print_exc()