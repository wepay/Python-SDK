class WePayError(Exception):
    """
    Raised when an error comes back in the API response from WePay.
    """
    def __init__(self, error_type, error_code, message):
        Exception.__init__(self, error_type, error_code, message)