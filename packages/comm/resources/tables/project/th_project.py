#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name')
        r.fieldcell('description', width='auto')
        r.fieldcell('app_url', width='25em')
        r.fieldcell('repository_url', width='25em')
        r.fieldcell('developer_id')

    def th_order(self):
        return 'name'

    def th_query(self):
        return dict(column='name', op='contains', val='')

class ViewDevelopers(View):

    def th_options(self):
        return dict(virtualStore=False, addrow=False, delrow=False)
        
class ViewFromDeveloper(View):

    def th_options(self):
        return dict(searchOn=False)

class Form(BaseComponent):
    py_requires="gnrcomponents/attachmanager/attachmanager:AttachManager"

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top', height='30%', datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('name')
        fb.field('description')
        fb.field('app_url')
        fb.field('repository_url')
        fb.field('developer_id')
        self.projectAttachments(bc.contentPane(region='center'))

    def projectAttachments(self,pane):
        pane.attachmentMultiButtonFrame()

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

class FormDevelopers(Form):

    def th_options(self):
        return dict(readOnly=True)