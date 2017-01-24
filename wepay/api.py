import urllib
import json
from wepay.exceptions import WePayError


class WePay(object):

    """
    A client for the WePay API.
    """

    def __init__(
            self, production=True, access_token=None, api_version=None,
            request_timeout=30):
        """
        :param bool production: When ``False``, the ``stage.wepay.com`` API
            server will be used instead of the default production.
        :param str access_token: The access token associated with your
            application.
        """
        import requests
        self.requests = requests
        self.access_token = access_token
        self.api_version = api_version
        self.request_timeout = request_timeout

        if production:
            self.api_endpoint = "https://wepayapi.com/v2"
            self.browser_endpoint = "https://www.wepay.com/v2"
        else:
            self.api_endpoint = "https://stage.wepayapi.com/v2"
            self.browser_endpoint = "https://stage.wepay.com/v2"

    def call(self, uri, params=None, token=None, risk_token=None, client_ip=None):
        """
        Calls wepay.com/v2/``uri`` with ``params`` and returns the JSON
        response as a python dict. The optional token parameter will override
        the instance's access_token if it is set.

        :param str uri: The URI on the API endpoint to call.
        :param dict params: The parameters to pass to the URI.
        :param str token: Optional override for this ``WePay`` object's access
            token.
        :param str risk_token: Optional WePay-Risk-Token for this API call.
        :param str client_ip: Optional Client-IP for this API call.
        """

        headers = {'Content-Type': 'application/json',
                   'User-Agent': 'WePay Python SDK'}
        url = self.api_endpoint + uri

        if self.access_token or token:
            headers['Authorization'] = 'Bearer ' + \
                (token if token else self.access_token)

        if self.api_version:
            headers['Api-Version'] = self.api_version

        if risk_token:
            headers['WePay-Risk-Token'] = risk_token

        if client_ip:
            headers['Client-IP'] = client_ip

        if params:
            params = json.dumps(params)

        try:
            response = self.requests.post(
                url, data=params, headers=headers,
                timeout=self.request_timeout)
            return response.json()
        except:
            if 400 <= response.status_code <= 599:
                raise Exception('Unknown error. Please contact support@wepay.com')

    def get_authorization_url(self, redirect_uri, client_id, options=None,
                              scope=None):
        """
        Returns a URL to send the user to in order to get authorization.
        After getting authorization the user will return to redirect_uri.
        Optionally, scope can be set to limit permissions, and the options
        dict can be loaded with any combination of state, user_name
        or user_email.

        :param str redirect_uri: The URI to redirect to after a authorization.
        :param str client_id: The client ID issued by WePay to your app.
        :keyword dict options: Allows for passing additional values to the
            authorize call, aside from scope, redirect_uri, and etc.
        :keyword str scope: A comma-separated string of permissions.
        """
        if not options:
            options = {}
        if not scope:
            scope = "manage_accounts,collect_payments," \
                    "view_user,preapprove_payments," \
                    "manage_subscriptions,send_money"

        options['scope'] = scope
        options['redirect_uri'] = redirect_uri
        options['client_id'] = client_id

        return self.browser_endpoint + '/oauth2/authorize?' + \
            urllib.urlencode(options)

    def get_token(
            self, redirect_uri, client_id, client_secret,
            code, callback_uri=None):
        """
        Calls wepay.com/v2/oauth2/token to get an access token. Sets the
        access_token for the WePay instance and returns the entire response
        as a dict. Should only be called after the user returns from being
        sent to get_authorization_url.

        :param str redirect_uri: The same URI specified in the
            :py:meth:`get_authorization_url` call that preceeded this.
        :param str client_id: The client ID issued by WePay to your app.
        :param str client_secret: The client secret issued by WePay
            to your app.
        :param str code: The code returned by :py:meth:`get_authorization_url`.
        :param str callback_uri: The callback_uri you want to receive IPNs for
            this user on.
        """
        params = {
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
        }
        if callback_uri:
            params.update({'callback_uri': callback_uri})
        response = self.call('/oauth2/token', params)
      
        # The call to /oauth2/token should return an access_token
        # if the access_token was not returned, then an error occured
        # we need to raise this error, 
        # otherwise this will die when trying to use the 'access_token' field
        if 'access_token' not in response:
            raise WePayError(response['error'], response['error_code'], response['error_description'])

        self.access_token = response['access_token']
        return response
