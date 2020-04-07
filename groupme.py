import logging
import json
import os
import requests
from datetime import datetime, date, timedelta

class APIAuthException(Exception):
    pass

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)


class GroupMe:

    def __init__(self, api_token=os.environ['groupme_token']):
        self.api_url = "https://api.groupme.com/v3"
        self.api_token = api_token

    def _api_request(self, endpoint, params=None):
        """ helper to do API GET calls """
        
        if params:
            response = requests.get(url=f"{self.api_url}/{endpoint}", params=params)
        else:
            response = requests.get(url=f"{self.api_url}/{endpoint}")
        code = response.status_code
        if 200 <= code < 300:
            logging.debug(f"API call: {self.api_url}/{endpoint} | {code}")
            encoding = response.encoding
            raw = response.content
            return json.loads(raw.decode(encoding))
        elif code > 500:
            raise APIAuthException
        else:
            logging.error(f"ERROR: Bad API call: {self.api_url}/{endpoint} | {code}")

    def _api_request_post(self, endpoint, data, headers=None):
        """ helper to do API POST calls """

        all_headers = {"Authorization": self.auth_header}
        if headers:
            for header in headers:
                all_headers[header] = headers[header]

        response = requests.post(url=f"{self.api_url}/{endpoint}", headers=all_headers, data=data)
        code = response.status_code
        if 200 <= code < 300:
            logging.debug(f"API POST call: {self.api_url}/{endpoint} | {code}")
            encoding = response.encoding
            raw = response.content
            return json.loads(raw.decode(encoding))
        elif code > 500:
            raise APIAuthException
        else:
            logging.error(f"ERROR: Bad API POST call: {self.api_url}/{endpoint} | {code}")

    def get_groups(self):
  
        params = {"token": self.api_token}
        response = self._api_request("groups", params=params)
        if response is not None and response != []:
            return response['response']

    def get_1page_group_messages(self, groupid, page=0):

        params = {"token": self.api_token, "limit": 20}
        
        if page:
            params["before_id"] = page
        
        response = self._api_request(f"groups/{groupid}/messages", params=params)
        if response is not None and response != []:
            return response['response']['messages']
        
