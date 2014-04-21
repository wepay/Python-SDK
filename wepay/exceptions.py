class WePayError(Exception):
    """
    Raised when an error comes back in the API response from WePay.
    """
    def __init__(self, error_type, error_code, message):
        super(WePayError, self).__init__(message)
        self.error_type = error_type
        self.error_code = error_code

    def __repr__(self):
        return "<%s:type=%r,code=%r,msg=%r>" % (
            self.__class__.__name__,
            self.error_type, self.error_code, self.message)
