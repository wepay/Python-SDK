WePay Python SDK
================

WePay's API allows you to easily add payments into your application.

For full documentation, see [WePay's developer documentation](https://www.wepay.com/developer).

For current and previous versions, see [PyPI](https://pypi.python.org/pypi/wepay).

Usage
-----
These examples use the simple [web.py](http://webpy.org/) application framework.

Setup
-----
Import the module:

    from wepay import WePay

Instantiate
-----

Create a new ``WePay`` instance. With no arguments, it will use the production
version of WePay ([www.wepay.com](https://www.wepay.com/)). If called with ``production=False`` then
it will use the staging version ([stage.wepay.com](https://stage.wepay.com/)) for testing:

    wepay = WePay()

If your user has already authorized your application and you still have the
access token, you can instantiate the SDK with the optional ``access_token``
parameter. Afterwards, ``wepay.call()`` will use the given token for the
authorization header:

    wepay = WePay(access_token=USERS_ACCESS_TOKEN)

To set an [API-Version](https://www.wepay.com/developer/reference/versioning) in the header with your call request, use::

    wepay = WePay(production=False, access_token=USERS_ACCESS_TOKEN, api_version=API_VERSION)

Get authorized
-----

Create an authorization url and redirect the user to it. The first parameter
is where the user will be redirected back to after they finish authorization.
The second is your ``CLIENT_ID`` which is provided by WePay:

    auth_url = wepay.get_authorization_url(web.ctx.homedomain + '/callback', CLIENT_ID)
    web.redirect(auth_url)

Handle the callback
-----

In your method for handling the redirect back to your site (in this case,
``/callback``), you will need to load the GET param ``code`` and then call
``get_token`` with it. ``CLIENT_SECRET`` is provided by WePay. The first
parameter of ``get_token`` should be the exact same string that was used
in ``get_authorization_url``:

    code = web.input(code='')['code']
    
    # make sure the first arg is exactly the same as the first arg
    # of get_authorization_url
    wepay.get_token(web.ctx.homedomain + '/callback', CLIENT_ID, CLIENT_SECRET, code)

The ``get_token`` method will automatically load the access token into the
``WePay`` instance so that all future API calls will use that token for
authorization. It also returns the entire response from the
``/v2/oauth2/token`` call if you need any additional data like the WePay ID.

Make some calls
-----

You are now ready to do anything on behalf of your user. Let's start by making
a new account:

    create_response = wepay.call('/account/create', {
        'name': 'kitty expenses fund',
        'description': 'all the money for my kitty'
    })

Now let's set a picture!:

    wepay.call('/account/modify', {
        'account_id': create_response['account_id'],
        'image_uri': 'http://www.placekitten.com/500/500'
    })

Redirect them to their account page to see it:

    web.redirect(create_response['account_uri'])

WePay Risk Headers
-----

You can supply WePay with risk-related information on every API call by passing the WePay-Risk-Token and Client-IP values to the `call` function:

```
wepay.call('/account/modify', {
    'account_id': create_response['account_id'],
    'image_uri': 'http://www.placekitten.com/500/500'
}, risk_token='123e4567-e89b-12d3-a456-426655440000', client_ip='100.166.99.123')
```

Detailed information regarding the Risk Headers can be found at the [WePay API Documentation](https://developer.wepay.com/reference/risk_headers).

Try it!
-----

These examples are put together into a working web app in
``wepay-example.py``. If you already have web.py installed, you can run it
by simply doing ``python wepay-example.py``. If you open the app in your
browser you should be redirected to WePay to authorize the app. After you
authorize, you should get redirected around a bit and end up on your new
account page with a kitty picture.

License
-----

MIT License
