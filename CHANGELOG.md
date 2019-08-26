# 0.3.4 Python SDK (2019-08-23)

## Bug Fixes
* **Error handling:** Fixed undefined local variable reference ([7e5e809](https://github.com/wepay/Python-SDK/commit/7e5e80950a17889fbba4328e90f60f212bdc4674)) 

# 0.3.3 Python SDK (2017-01-19)

## Bug Fixes
* **Version:** Updated version number to 0.3.3 ([682b761](https://github.com/wepay/Python-SDK/commit/682b761e8109c4329bc21bcab16d4091cd027c35))

## Breaking Changes
* **risk_token, client_ip:** Added optional risk_token and client_ip params to the API call function. ([682b761](https://github.com/wepay/Python-SDK/commit/682b761e8109c4329bc21bcab16d4091cd027c35))

# 0.3.2 Python SDK (2015-11-13)

## Bug fixes
* **Error handling:** Raise an error if request fails ([4e4ec5c](https://github.com/wepay/Python-SDK/commit/4e4ec5c2eba5cf0d61ce9a97474fdf6089bf8e16), [e7bbf2d](https://github.com/wepay/Python-SDK/commit/e7bbf2deb2514ec1133b0b48a70a809a949f6847), [ec775ab](https://github.com/wepay/Python-SDK/commit/ec775abfe4dc4ce282e238aa1e01038c217d300b))

# 0.3.1 Python SDK (2015-04-08)

## Bug fixes
* **Timeout:** Make request timeout configurable ([3554f2e](https://github.com/wepay/Python-SDK/commit/3554f2eced64fb730e367478ab73ba9036f88884))
* **Tests:** Add tests ([8d9a4d0](https://github.com/kevinjqiu/Python-SDK/commit/8d9a4d02ccc35a825fc40304eaef2aeed5807ec4))
* **Import:** Fix import during setup ([ecf99f6](https://github.com/wepay/Python-SDK/commit/ecf99f6f113c991156cefcb8bfc40cd2d08302bd))

# 0.3.0 Python SDK (2014-07-16)

## Breaking Changes
* **Exception:** Raise exception instead of WePayError ([e23b61c](https://github.com/wepay/Python-SDK/commit/e23b61c2a54567d16838efc6760123f639cb60f3))

# 0.2.4 Python SDK (2014-07-03)

## Bug Fixes
* **WePayError:** Revert to WePayError ([7383990](https://github.com/wepay/Python-SDK/commit/73839903d3d69dac6f0ace3ee1706de356df72d3))
* **Exception:** Raise exception ([cc7f664](https://github.com/wepay/Python-SDK/commit/cc7f664dcb94217e6682971ca84f0e3d6b33d6b1))


# 0.2.3 Python SDK (2014-05-14)

## Bug Fixes
* **Version:** Updated version number to 0.2.3

## Breaking Changes
* **callback_uri:** Support 'callback_uri' for /oauth/token API call ([0df3306](https://github.com/wepay/Python-SDK/commit/0df3306ab3ee15e411fb71e9e4ae360e8b6886e1))

# 0.2.2 Python SDK (2014-04-22)

## Bug Fixes
* **Version:** Updated version number to 0.2.2
* **ImportError:** Delayed import of 'requests' module to avoid ImportError ([ff1dc9c](https://github.com/wepay/Python-SDK/commit/ff1dc9c07389ef586b81fad08c86ce87f0979a55))
* **WePayError:** Fixed WePayError exception ([be85b2b](https://github.com/wepay/Python-SDK/commit/be85b2b4d4c2e3957f9b259e0d6ddd7070fcad9f))

# 0.2.1 Python SDK (2014-04-17)

## Bug Fixes
* **Version:** Updated version number to 0.2.1

## Breaking Changes
* **requests:** Updated urllib2 module to use requests -- part of setup.py now ([192cde7](https://github.com/wepay/Python-SDK/commit/192cde7e7d916b4ad72302e80e0671adee228bf9))

# 0.2.0 Python SDK (2014-04-16)

## Bug Fixes
* **Version:** Updated version number to 0.2.0 ([e36834a](https://github.com/wepay/Python-SDK/commit/e36834affa38232510d8091c8b84383c8762aa14))
* **setuptools:** Updated distutils module to setuptools ([e36834a](https://github.com/wepay/Python-SDK/commit/e36834affa38232510d8091c8b84383c8762aa14))

## Breaking Changes
* **error_code:** In [ff70c67](https://github.com/wepay/Python-SDK/commit/ff70c676978f7afdfd971f20447c2f4b2dcbca39), 'error_code' is a new parameter added before 'message' parameter
