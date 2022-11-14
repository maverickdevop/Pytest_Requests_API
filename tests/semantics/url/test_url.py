import json
import requests
import configuration
from src.schemas.semantics.url import GET_SCHEMA, GET_SCHEMA_PERIOD
from src.baseclasses.response import Response
from environment import ENV_OBJECT
from src.enums.global_enums import GlobalErrorMessages


class TestSemanticsURL:

    global URL
    URL = f"{ENV_OBJECT.get_base_url()}"

    def test_setup(self):

        global token
        
        payload = {'login': configuration.USER, 'password': configuration.PASSWORD}

        r = requests.post(url=URL + "/api/v1/auth", data=json.dumps(payload))
        token = r.json()['data']['access_token']

    def test_url_summary_day(self):

        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_Y
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1&limit=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE
        response.validate(GET_SCHEMA), GlobalErrorMessages.WRONG_JSON_SCHEMA.value

    def test_url_summary_period(self):

        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM_PERIOD,
                'date_to': configuration.DAY_TO_PERIOD,
                'search_system': configuration.SE_G
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1&limit=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE
        response.validate(GET_SCHEMA_PERIOD), GlobalErrorMessages.WRONG_JSON_SCHEMA.value

    def test_url_summary_document_and_query(self):

        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_Y,
                'document': configuration.DOCUMENT,
                'query': configuration.QUERY
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        url = []

        for item in r.json()['data']['items']:
            url.append(item['entity']['url'])

        print('URL list in Semantics/Documents API:', url[0:3])

        for item in url:
            assert configuration.DOCUMENT in item, GlobalErrorMessages.WRONG_DOCUMENT.value

    def test_url_summary_segment_filters(self):

        # Select segment query-group
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_Y,
                'query_group_id': configuration.QUERY_GROUP
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        # Select segment category
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_Y,
                'category_id': configuration.CATEGORY
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1&limit=10",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        category_id = []
        category_name = []

        for i in r.json()['data']['items']:
            category_id = i['category']['id']
            category_name = i['category']['name']

        print('Category ID in Semantics/Documents API:', category_id)
        print('Category Names in Semantics/Documents API:', category_name)

        assert category_id == int(configuration.CATEGORY) and category_name == configuration.CATEGORY_NAME, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

        # Select segment group
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_Y,
                'group_id': configuration.GROUP
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

    def test_url_metric_filters(self):

        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_Y,
                'ws1_from': configuration.WS1_FROM,
                'ws1_to': configuration.WS1_TO,
                'top3_prc_from': configuration.TOP3_FROM,
                'top3_prc_to': configuration.TOP3_TO,
                'p_traf_from': configuration.PTRAF_FROM,
                'p_traf_to': configuration.PTRAF_TO
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        ws1 = []
        top3 = []
        ptraf = []

        for item in r.json()['data']['items']:
            ws1.append(int(item['frequency']['ws1']))
            top3.append(float(item['top']['top3']))
            ptraf.append(float(item['potential_traffic']['traffic']))

        print('Documents WS1 list in Semantics/Documents API:', ws1)
        print('Documents TOP3 list in Semantics/Documents API:', top3)
        print('Documents Ptraf list in Semantics/Query API:', ptraf)

        for i in ws1:
            assert int(configuration.WS1_FROM) <= i <= int(
                configuration.WS1_TO), GlobalErrorMessages.WRONG_FILTER.value

        for i in top3:
            assert float(configuration.TOP3_FROM) <= i <= float(
                configuration.TOP3_TO), GlobalErrorMessages.WRONG_FILTER.value

        for i in ptraf:
            assert float(configuration.PTRAF_FROM) <= i <= float(
                configuration.PTRAF_TO), GlobalErrorMessages.WRONG_FILTER.value

        # AVG TOP30 Yandex
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_Y,
                'avg_position_top30_from': configuration.AVG_TOP30_FROM,
                'avg_position_top30_to': configuration.AVG_TOP30_TO
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        avg_top30 = []

        for item in r.json()['data']['items']:
            avg_top30.append(float(item['top']['position_top30']))

        print('Documents AVG.TOP30 list in Semantics/Documents API:', avg_top30)

        for i in avg_top30:
            assert int(configuration.AVG_TOP30_FROM) <= i <= int(
                configuration.AVG_TOP30_TO), GlobalErrorMessages.WRONG_FILTER.value

    def test_url_sorting(self):

        # WS Sorting DESC
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_G,
                'sort': 'ws1-DESC'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        ws1 = []

        for i in r.json()['data']['items']:
            ws1.append(int(i['frequency']['ws1']))

        for i in range(len(ws1) - 1):
            assert ws1[i] >= ws1[i + 1], GlobalErrorMessages.WRONG_SORT.value

        # WS Sorting ASC
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_G,
                'sort': 'ws1-ASC'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        ws1 = []

        for item in r.json()['data']['items']:
            ws1.append(int(item['frequency']['ws1']))

        for item in range(len(ws1) - 1):
            assert ws1[item] <= ws1[item + 1], GlobalErrorMessages.WRONG_SORT.value

        # TOP3 Sorting DESC
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_G,
                'sort': 'top3_prc-DESC'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        top3 = []

        for i in r.json()['data']['items']:
            top3.append(float(i['top']['top3']))

        for i in range(len(top3) - 1):
            assert top3[i] >= top3[i + 1], GlobalErrorMessages.WRONG_SORT.value

        # TOP3 Sorting ASC
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_G,
                'sort': 'top3_prc-ASC'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        top3 = []

        for i in r.json()['data']['items']:
            top3.append(float(i['top']['top3']))

        for item in range(len(top3) - 1):
            assert top3[item] <= top3[item + 1], GlobalErrorMessages.WRONG_SORT.value

        # PTraf Sorting DESC
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_G,
                'sort': 'p_traf-DESC'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        ptraf = []

        for i in r.json()['data']['items']:
            ptraf.append(float(i['potential_traffic']['traffic']))

        for i in range(len(ptraf) - 1):
            assert ptraf[i] >= ptraf[i + 1], GlobalErrorMessages.WRONG_SORT.value

        # PTraf Sorting ASC
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM,
                'date_to': configuration.DAY_TO,
                'search_system': configuration.SE_G,
                'sort': 'p_traf-ASC'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        ptraf = []

        for i in r.json()['data']['items']:
            ptraf.append(float(i['potential_traffic']['traffic']))

        for i in range(len(ptraf) - 1):
            assert ptraf[i] <= ptraf[i + 1], GlobalErrorMessages.WRONG_SORT.value

    def test_url_limits(self):

        # Limit 5 elements on page
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM_PERIOD,
                'date_to': configuration.DAY_TO_PERIOD,
                'search_system': configuration.SE_Y,
                'limit': '5'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        count_keyword = len(r.json()['data']['items'])
        print("Count of Query with limit 5:", count_keyword)

        assert count_keyword == 5, GlobalErrorMessages.WRONG_COUNTER.value

        # Limit 25 elements on page
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM_PERIOD,
                'date_to': configuration.DAY_TO_PERIOD,
                'search_system': configuration.SE_Y,
                'limit': '25'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        count_keyword = len(r.json()['data']['items'])
        print("Count of Query with limit 25:", count_keyword)

        assert count_keyword == 25, GlobalErrorMessages.WRONG_COUNTER.value

        # Limit 100 elements on page
        data = {'project_id': configuration.PROJECT_ID,
                'date_from': configuration.DAY_FROM_PERIOD,
                'date_to': configuration.DAY_TO_PERIOD,
                'search_system': configuration.SE_Y,
                'limit': '100'
                }

        r = requests.get(url=URL + "/api/v1/semantics/dashboard/documents?ch=1",
                         headers={'Authorization': 'Bearer' + ' ' + token},
                         params=data)

        response = Response(r)

        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value

        count_keyword = len(r.json()['data']['items'])
        print("Count of Query with limit 100:", count_keyword)

        assert count_keyword == 100, GlobalErrorMessages.WRONG_COUNTER.value