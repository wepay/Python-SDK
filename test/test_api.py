from mock import Mock, call
from nose.tools import eq_
from wepay import WePay


def test_default_timeout_is_passed_to_requests():
    api = WePay()
    api.requests = Mock()
    api.call('/some_uri')
    eq_([call('https://wepayapi.com/v2/some_uri',
              headers={'Content-Type': 'application/json',
                       'User-Agent': 'WePay Python SDK'},
              data=None, timeout=30)],
        api.requests.post.call_args_list)


def test_customized_timeout_is_passed_to_requests():
    api = WePay(request_timeout=45)
    api.requests = Mock()
    api.call('/some_uri')
    eq_([call('https://wepayapi.com/v2/some_uri',
              headers={'Content-Type': 'application/json',
                       'User-Agent': 'WePay Python SDK'},
              data=None, timeout=45)],
        api.requests.post.call_args_list)
