# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):

    @metadata(for_update=True)
    def touch_fix_evalbag(self, record=None, old_record=None, **kwargs):
        "Fix Bag evaluationGrid"
        if not record['value_bag']:
            return
        for node in record['value_bag'].nodes:
            value_bag = node.value
            value_keys = [v for v in value_bag.keys() if v.startswith('value_')]
            for v in value_keys:
                value = int(v.replace("value_",""))
                value_bag['value'] = value
        self.raw_update(record,old_record)

