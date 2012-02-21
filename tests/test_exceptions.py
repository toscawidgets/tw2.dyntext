import tw2.core as twc
import tw2.dyntext

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

def test_exception_nodata_url():
    w = tw2.dyntext.DynamicTextWidget(id='foobar')
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'DynamicTextWidget data_url parameter must be set')

def test_exception_bad_data_url():
    w = tw2.dyntext.DynamicTextWidget(id='foobar', data_url=dict())
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'DynamicTextWidget data_url parameter must be a string')
