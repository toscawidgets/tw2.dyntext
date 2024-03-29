from tw2.core.testbase import  WidgetTest
import tw2.dyntext

class TestPollingDemoWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = tw2.dyntext.PollingDynamicTextWidget

    # Initilization args. go here
    attrs = {'id' : 'affected_count'}
    params = {'wrap': 'div', 'data_url' : '/stats/affected_count'}
    expected = """<div id="affected_count"></div>"""


class TestDemoWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = tw2.dyntext.DynamicTextWidget

    # Initilization args. go here
    attrs = {'id' : 'affected_count'}
    params = {'initial_text' : 'test'}
    expected = """<span id="affected_count">test</span>"""
