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
