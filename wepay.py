import urllib,urllib2,json

class WePay(object):
    """A client for the WePay API"""
    
    def __init__(self, production=True, access_token=None):
        """If production is False, then stage.wepay.com will be used.
        If access_token is set then all calls will use that token for
        the Authorization header"""
        self.access_token = access_token
        if production:
            self.wepay_url = "https://www.wepay.com/v2"
        else:
            self.wepay_url = "https://stage.wepay.com/v2"
    
    def call(self, uri, params=None, token=None):
        """Calls wepay.com/v2/{uri} with {params} and returns the json
        response as a python dict. Will use POST if {token} or {self.access_token} is set."""
        
        url = self.wepay_url + uri
        payload = ''
        if self.access_token or token:
            headers = {
                'Authorization': 'Bearer ' + (token if token else self.access_token),
                'Content-Type' : 'application/x-www-form-urlencoded'
            }
            if params:
                params = urllib.urlencode(params)
        else:
            url += "?" + urllib.urlencode(params)
            headers = {}
            params = None
        
        request = urllib2.Request(url, params, headers)
        try:
            response = urllib2.urlopen(request).read()
            return json.loads(response)
        except urllib2.HTTPError as e:
            print dir(request)
            print request.data
            response = json.loads(e.read())
            raise WePay.WePayError(response['error'], response['error_description'])
            
    def get_authorization_url(self, redirect_uri, client_id, options = {}, scope="manage_accounts,collect_payments,view_balance,view_user,refund_payments"):
        """Returns a URL to send the user to in order to get authorization.
        After getting authorization the user will return to redirect_uri.
        Optionally, scope can be set to limit permissions, and the options
        dict can be loaded with any combination of state, user_name or user_email."""
        options['scope'] = scope
        options['redirect_uri'] = redirect_uri
        options['client_id'] = client_id
        
        return self.wepay_url + '/oauth2/authorize?' + urllib.urlencode(options)
    
    def get_token(self, redirect_uri, client_id, client_secret, code):
        """Calls wepay.com/v2/oauth2/token to get an access token. Sets the access_token
        for the WePay instance and returns the entire response as a dict. Should only be
        called after the user returns from being sent to get_authorization_url."""
        params = { 'redirect_uri'  : redirect_uri,
                   'client_id'     : client_id,
                   'client_secret' : client_secret,
                   'code'          : code }
        response = self.call('/oauth2/token', params)
        self.access_token = response['access_token']
        return response
        
    class WePayError(Exception):
        def __init__(self, type, message):
            Exception.__init__(self, message)
            self.type = type