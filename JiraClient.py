import requests
import Config
import json
import logging

class Jira(object):
    def __init__(self):
        self.s = requests.Session()
        self.s.auth = (Config.settings['jira_username'], Config.settings['jira_password'])
        logging.basicConfig(filename='./error.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

    def HasLinkedItem(self, issue, title):
        s = self.s
        query = Config.settings['jira_api'] + 'issue/' + issue + Config.settings['jira_remotelink']
        try:
            response = s.get(query)
            json_data = json.loads(response.text)
            for links in json_data:
                if title in links['object']['title']:
                    return True
        except Exception as ex:
            logging.error(ex)
            pass
        return False

    def AddLinkedItem(self, title, url, issue):
        s = self.s
        json_data = '{ ' \
                    '"object": { "url":"' + url + '",' \
                    ' "title":"Change '+ title + '"  }' \
                    '}'
        query = Config.settings['jira_api'] + 'issue/' + issue + Config.settings['jira_remotelink']
        headers = {'content-type': 'application/json'}
        response = s.post(query,data=json_data,headers=headers)