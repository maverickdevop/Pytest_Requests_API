from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:
    """ Basics for response / validation / cookie and headers etc. """

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.response_lenght = len(response.json())
        self.response_cookie = response.cookies
        self.response_header = response.headers

    def get_cookie(self, cookie_name):
        assert cookie_name in self.response_cookie, GlobalErrorMessages.WRONG_COOKIE.value
        return self.response_cookie[cookie_name]

    def get_header(self, header_name):
        assert header_name in self.response_header, GlobalErrorMessages.WRONG_HEADER.value
        return self.response_header[header_name]

    def validate(self, schema):
        validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def assert_lenght(self, lenght):
        assert self.response_lenght == lenght, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested URL: {self.response.url} \n" \
            f"Response body: {self.response_json}"