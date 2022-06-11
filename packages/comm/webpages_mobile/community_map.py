# -*- coding: utf-8 -*-
from gnr.core.gnrbag import Bag
class GnrCustomWebPage(object):
    py_requires='th/th:TableHandler'

    def main(self, root, **kwargs):
        bc = root.borderContainer(datapath='main')               
        th_dev = bc.contentPane(region='center', margin='2px').plainTableHandler(
                        nodeId='developers',
                        table='comm.developer', 
                        viewResource='ViewMap', 
                        groupable=True,
                        configurable=False,
                        view_store_onStart=True,
                        addrow=False, delrow=False,
                        pbl_classes='*')
        map_cp = bc.contentPane(region='bottom', height='50%').GoogleMap( 
                        height='100%',
                        map_type='roadmap',
                        centerMarker=True,
                        nodeId='maps',
                        autoFit=True)      
        bc.dataController(""" 
                            if(!m.map){
                                        return;
                                    }
                            m.gnr.clearMarkers(m);
                            var that = this;
                            store.forEach(function(n){
                                // console.log(n);
                                m.gnr.setMarker(m, n.attr._pkey, n.attr.position, {title:n.attr.tg_username, 
                                                                                    onClick:function(marker_name, e){
                                                                                        //  console.log("single",marker_name,e);
                                                                                         grid.setSelectedId(marker_name);
                                                                                            },
                                                                                   // labelContent: n.attr.tg_username,
                                                                                   // labelAnchor: new google.maps.Point(15, 0),
                                                                                   // labelClass: "markerlabel" // the CSS class for the label
                                                                                    }
                                                );
                            }, 'static');
                         """,
                            m=map_cp,
                            store='^#developers.view.store',
                            grid=th_dev.view.grid.js_widget,
                            _delay=100)