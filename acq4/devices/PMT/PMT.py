# -*- coding: utf-8 -*-
from __future__ import absolute_import
from acq4.devices.OptomechDevice import OptomechDevice
from acq4.devices.DAQGeneric import DAQGeneric

class PMT(DAQGeneric, OptomechDevice):
    def __init__(self, dm, config, name):
        self.omConf = {}
        for k in ['parentDevice', 'transform']:
            if k in config:
                self.omConf[k] = config.pop(k)
        DAQGeneric.__init__(self, dm, config, name)
        OptomechDevice.__init__(self, dm, config, name)

    def getFilterDevice(self):
        # return parent filter device or None
        if 'Filter' in self.omConf['parentDevice'] :
            return self.omConf['parentDevice']
        else:
            return None
        
        
