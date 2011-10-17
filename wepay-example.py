import web
from wepay import WePay

CLIENT_ID = ''
CLIENT_SECRET = ''
IN_PRODUCTION = False

urls = (
    '/', 'index',
    '/callback(.*)', 'callback'
)
app = web.application(urls, globals())

class index:
    def GET(self):
        wepay = WePay(IN_PRODUCTION)
        
        # redirect to wepay for authorization
        web.redirect(wepay.get_authorization_url(web.ctx.homedomain + '/callback', CLIENT_ID))

class callback:
    def GET(self, query):
        wepay = WePay(IN_PRODUCTION)
        code = web.input(code='')['code']
        try:
            # try to get a token with our code
            wepay.get_token(web.ctx.homedomain + '/callback', CLIENT_ID, CLIENT_SECRET, code)
            
            # make a new account
            create_response = wepay.call('/account/create', { 'name': 'kitty expenses fund', 'description': 'all the money for my kitty' })
            
            # give the account a new picture
            wepay.call('/account/modify', { 'account_id': create_response['account_id'], 'image_uri': 'http://www.placekitten.com/500/500' })
            
            # redirect to the new account
            web.redirect(create_response['account_uri'])
            
        except WePay.WePayError as e:
            return "Received a WePay Error: " + repr(e)
        
if __name__ == "__main__":
    app.run()