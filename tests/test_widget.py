from tw2.core.testbase import  WidgetTest
from tw2.dyntext import DynamicTextWidget
from nose.tools import raises

class TestDemoWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = DynamicTextWidget

    # Initilization args. go here
    attrs = {'id' : 'affected_count'}
    params = {'data_url' : '/stats/affected_count'}
    expected = """<span id="affected_count"></span>"""
