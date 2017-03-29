import json
import Config
import requests


class SwarmActivityItem(object):
    def __init__(self, id, url, change, description ):
        self.id = id
        self.url = url
        self.change = change
        self.description = description

    def __str__(self):
        return ("id: " + str(self.id) + "\n"
         "url: " + str(self.url) +"\n"
         "change: " + str(self.change) +"\n"
         "description: " + str(self.description))+"\n"

class Swarm(object):
    def __init__(self):
        self.s = requests.Session()
        self.s.auth = (Config.settings['swarm_username'], Config.settings['swarm_password'])

    def __do_query(self, query_string):
        s = self.s
        response = s.get(query_string)
        lastSeen = 0;
        activity = []
        if "200" in str(response.status_code):
            json_data = json.loads(response.text)
            for item in json_data['activity']:
                activity.append(SwarmActivityItem(str(item['id']), str(item['url']), str(item['change']), item['description'].split(':')[0]))
            lastSeen = json_data["lastSeen"]

        while lastSeen > Config.settings['swarm_jira_start'] :
            response = s.get(query_string+ "&after=" + str(lastSeen))
            json_data = json.loads(response.text)
            if not json_data["activity"]:
                return activity
            if "200" in str(response.status_code):
                for item in json_data['activity']:
                    activity.append(SwarmActivityItem(str(item['id']), str(item['url']), str(item['change']),
                                                      item['description'].split(':')[0]))
                lastSeen = json_data["lastSeen"]
        return activity

    def LoadUserChanges(self):
        activity_url = Config.settings['swarm_server'] + Config.settings['swarm_activity'] + Config.settings['swarm_user_stream']
        return self.__do_query(activity_url)

    def LoadAllChanges(self):
        activity_url = Config.settings['swarm_server'] + Config.settings['swarm_activity'] #+ "/after=" + lastSeen
        return self.__do_query(activity_url)