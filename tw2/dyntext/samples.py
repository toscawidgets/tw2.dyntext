"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import widgets
import json
import random
import webob

class DemoDynamicTextWidget(widgets.DynamicTextWidget):
    # Provide default parameters, value, etc... here
    # default = <some-default-value>
    data_url = '/dynamic_text_demo'
    
    pass

    @classmethod
    def request(cls, req):
        lottery_numbers = ", ".join([str(random.randint(1,100)) for x in range(5)])

        resp = webob.Response(request=req, content_type="application/json")
        resp.body = json.dumps({'text': lottery_numbers})

        return resp

import tw2.core as twc
mw = twc.core.request_local()['middleware']
mw.controllers.register(DemoDynamicTextWidget, 'dynamic_text_demo')
