import tw2.core as twc

# tw2.jquery imports
from tw2.jquery import jquery_js
import json

setup_call = twc.js_function('setupPollingDynText')

class DynamicTextWidget(twc.Widget):
    template = "mako:tw2.dyntext.templates.dyntext"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/dyntext.js'),
        jquery_js
    ]

    data_url = twc.Param('(str) URL where JSON data should be pulled from', default=None)

    interval = twc.Param('(int) Polling interval in milliseconds', default=5000)

    initial_text = twc.Param('Initial text to place in the widget', default='')

    def j(cls, attr):
       return json.dumps(getattr(cls, attr))

    def prepare(self):
        if self.data_url is None:
            raise ValueError, "DynamicTextWidget data_url parameter must be set"
        elif 'str' not in str(type(self.data_url)):
            raise ValueError, "DynamicTextWidget data_url parameter must be a string"

        super(DynamicTextWidget, self).prepare()
        # put code here to run just before the widget is displayed
        self.selector = self.attrs['id'].replace(':', '\\:')
        self.add_call(setup_call(self.selector, self.data_url, self.interval))
