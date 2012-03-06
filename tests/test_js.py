import tw2.core as twc
import tw2.dyntext

from nose.tools import eq_

def request_local_tst():
    global _request_local, _request_id
# if _request_id is None:
# raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()

def test_js_call():
    w = tw2.dyntext.PollingDynamicTextWidget(id='foobar', data_url="/herp/derp")
    w.display()

    js_calls = filter(lambda x: "JSFuncCall" in str(x), w.resources)

    assert(len(js_calls) > 0)

    for js_call in js_calls:
        js = js_call.req()
        js.prepare()
        eq_(js.src, """setupPollingDynText("foobar", "/herp/derp", 5000)""")
