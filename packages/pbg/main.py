#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='Python Biella Group package',sqlschema='pbg',sqlprefix=True,
                    name_short='!![en]PBG', name_long='!![en]Python Biella Group', name_full='!![en]Python Biella Community')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
