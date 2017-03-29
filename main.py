import sys
import requests
import json
from requests import Request, Session
from requests.auth import HTTPBasicAuth
import argparse
from SwarmClient import Swarm
from JiraClient import Jira
import Config


if __name__ == '__main__':
    swarm = Swarm()
    jira = Jira()
    parser = argparse.ArgumentParser( epilog="WARRNING: -a, --all will update all Jiras in the search range specified in the config!!!")
    parser.add_argument("-u", "--user", help="Update user Jiras",
                        action="store_true")
    parser.add_argument("-a", "--all", help="Update all Jiras",
                        action="store_true")
    args = parser.parse_args()
    if args.user or not len(sys.argv) > 1:
        changes = swarm.LoadUserChanges()

    elif args.all:
        changes = swarm.LoadAllChanges()

    for item in changes:

        print jira.HasLinkedItem(item.description, item.change)

        if not jira.HasLinkedItem(item.description, item.change):
            print str(item.change) + " " + str(item.description) + " " + Config.settings['swarm_server'] + str(
                item.url) + "  Added the link to the Jira."
            jira.AddLinkedItem(str(item.change), Config.settings['swarm_server'] + str(item.url), str(item.description))
        else:
            print str(item.change) + " " + str(item.description) + " " + Config.settings['swarm_server'] + str(
                item.url) + "  The remote link already exists."
