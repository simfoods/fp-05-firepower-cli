    
#********************************************************************
#      File:    base.py
#      Author:  Sam Strachan / Huxley Barbee
#
#      Description:
#       Base class for constructing estreamer request messages
#
#      Copyright (c) 2017 by Cisco Systems, Inc.
#
#       ALL RIGHTS RESERVED. THESE SOURCE FILES ARE THE SOLE PROPERTY
#       OF CISCO SYSTEMS, Inc. AND CONTAIN CONFIDENTIAL  AND PROPRIETARY
#       INFORMATION.  REPRODUCTION OR DUPLICATION BY ANY MEANS OF ANY
#       PORTION OF THIS SOFTWARE WITHOUT PRIOR WRITTEN CONSENT OF
#       CISCO SYSTEMS, Inc. IS STRICTLY PROHIBITED.
#
#*********************************************************************/

import struct
import estreamer.definitions as definitions
import estreamer
from sys import getsizeof
import estreamer.definitions as definitions
import estreamer.settings as settings
import struct
import argparse
import os
import signal
import sys
import time
import estreamer

WORKING_DIRECTORY = os.path.abspath( os.path.dirname(__file__) + '/..')
sys.path.append(WORKING_DIRECTORY) 

class Base( object ):
    """Base message encoder"""
    def __init__( self, messageType, packFormat ):
        self.data = [ definitions.MESSAGE_VERSION, 0, 0 ]
        self.messageType = messageType
        self.packFormat = packFormat
        self.messageLength = 0

    def increaseLength(self, size):
        self.messageLength += size
 
    def setLength(self, size) :
        self.messageLength = size

    def set( self, index, newData ):
        """Allows the setting of a precise piece of data in the message rather
        than through direct access to self.data"""
        self.data[ index ] = newData



    def append( self, moreData, size, extraFormat=None ):
        """Helper function to append additional data into a wire message."""
        self.data.append( moreData )
        self.messageLength += size

        if extraFormat:
            self.packFormat += extraFormat



    def fixData( self ):
        """Sets the message type and length. Must be called just before
        getWireData"""
        self.data[1] = self.messageType
        self.data[2] = self.messageLength



    def getWireData( self ):
        """
        Performs any necessary final adjustments to the message (setting length
        etc) and then formats as a series of bytes ready for transmission
        """

        self.fixData()
        jsonSettings = estreamer.Settings.create( WORKING_DIRECTORY + "/request.conf" )
#        self.increaseLength(len(jsonSettings.store))
#        self.setLength(222)
        print 'data in base.py'
        print self.packFormat
        print self.data
        
        return struct.pack( self.packFormat, *self.data ) 
