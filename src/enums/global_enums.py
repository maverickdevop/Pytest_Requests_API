from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected!"
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected!"
    WRONG_JSON_SCHEMA = "JSON schema is not equal to expected schema!"
    WRONG_COOKIE = "Cookie-name is not contain in request!"
    WRONG_HEADER = "Header-name is not contain in request!"
    WRONG_COUNTER = "Elements counter is wrong!"
    WRONG_FILTER = "Metric not matched with filter!"
    WRONG_SORT = "Wrong sorting by metric!"
    WRONG_CATALOG = "Wrong catalog ID in Segmentation!"
    WRONG_DOCUMENT = "Document not contains in list!"
    WRONG_KEYWORD = "Query not contains in list!"
    WRONG_EQL = "URL not equal to expected filter!"
    WRONG_DATA = "Expected data not contains in list!"
