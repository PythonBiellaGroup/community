# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Menu(object):
    def config(self,root,**kwargs):
        root.packageBranch(u"!![en]Community", pkg="comm")
        root.packageBranch(u"!![en]Surveys", pkg="srvy", tags='admin')
        if self.db.application.getPreference('enable_social', pkg='comm'):
            root.packageBranch(u"!![en]Social", pkg="social", tags='admin')
            root.packageBranch(u"!![en]Video", pkg="video", tags='admin')
        if self.db.application.getPreference('enable_dem', pkg='comm'):
            root.packageBranch(u"!![en]DEM", pkg="dem", tags='admin')
        root.packageBranch(u"!![en]E-mail", pkg="email", tags='admin')
        root.packageBranch(u"!![en]Administration", tags="superadmin,_DEV_", pkg="adm")
        root.packageBranch(u"!![en]System", tags="_DEV_", pkg="sys")
        root.packageBranch("!![en]Dashboard", pkg="biz")

    @metadata(group_code='COMM')
    def config_community(self,root,**kwargs):
        root.thpage("!![en]My profile", table='comm.developer', formResource='FormProfile',
                            pkey=self.db.currentEnv.get('developer_id'), form_locked=False)
        root.webpage(u"!![en]Community", filepath="/comm/community_map")
        root.thpage(u"!![en]Suggestions", table="comm.suggestion")
        root.thpage(u"!![en]Projects", table="comm.project", 
                            viewResource='ViewDevelopers', formResource='FormDevelopers')
        root.thpage(u"!![en]Events", table="comm.event_series",
                            viewResource='ViewDevelopers', formResource='FormDevelopers')

    @metadata(group_code='SUPP')
    def config_supporters(self,root,**kwargs):
        root.thpage("!![en]My profile", table='comm.developer', formResource='FormProfile',
                            pkey=self.db.currentEnv.get('developer_id'), form_locked=False)
        root.thpage(u"!![en]Suggestions", table="comm.suggestion")
        root.webpage(u"!![en]Community", filepath="/comm/community_map")
        root.thpage(u"!![en]Projects", table="comm.project", 
                            viewResource='ViewSupporters', formResource='FormSupporters')
        root.thpage(u"!![en]Events", table="comm.event_series", 
                            viewResource='ViewSupporters', formResource='FormSupporters')