from tw2.core.testbase import  WidgetTest
import tw2.dyntext

class TestDemoWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = tw2.dyntext.DynamicTextWidget

    # Initilization args. go here
    attrs = {'id' : 'affected_count'}
    params = {'data_url' : '/stats/affected_count'}
    expected = """<span id="affected_count"></span>"""
