# encoding: utf-8
from gnr.core.gnrdecorator import public_method

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('project', pkey='id', name_long='!![en]Project', 
                        name_plural='!![en]Projects', caption_field='name')
        self.sysFields(tbl)
        
        tbl.column('name', name_long='!![en]Name')
        tbl.column('description', name_long='!![en]Description', name_short='!![en]Descr.')
        tbl.column('app_url', name_long='!![en]Project URL')
        tbl.column('repository_url', name_long='!![en]Repository URL')
        tbl.column('developer_id',size='22', group='_', name_long='!![en]Developer'
                    ).relation('developer.id', relation_name='projects', mode='foreignkey', onDelete='cascade')