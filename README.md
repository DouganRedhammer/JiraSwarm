# JiraSwarm
Updates Jira Tickets with Helix Swarm Change Items

## Dependencies
* argparse
* requests
* json
* sys

## Installation

Install dependencies

    pip install requests

Update config.json settings
    
Clone or download JiraSwarm zip, then 
````
    $ python main.py
````


## Config settings
Must update the config.json before use.

The username to your Jira account
    
    "jira_username": "your-jira-username"
    
The password to your Jira login
    
    "jira_password": "your-jira-password"

The location of the Jira server with api

    "jira_api": "http://jira-server.your-server.com/rest/api/2/"

The you want to be added to Jira comments (Deprecated)
    
    "jira_author_name": "Name you want to display in Jira"
    
Jira api to query Issue Links.

    "jira_remotelink":"/remotelink"
    
The location of your Helix Swarm server

    "swarm_server":"http://swarmserver.your-server.com"

Main query string. Replace version or max results only.
    
    "swarm_activity": "/api/v5/activity?max=100"

Limits the query to your account changes. 
This can be found by searching for your login ID in the activity api request.
http://swarmserver.yourserver.com/api/v5/activity?
default pattern is: user-yourusername
    
    "swarm_user_stream": "&stream=user-yourSwarmUsernameHere"
ex:
    
    "swarm_user_stream": "&stream=user-douganredhammer"

The username for your swarm user account
    
    "swarm_username": "your-swarm-username"

The password to your swarm login    
    
    "swarm_password": "your-swarm-password"

Integer of approximate termination of swarm pagination
    
    "swarm_jira_start": 1

Example Config
````json
{
    "jira_username": "bob",
    "jira_password": "123456",
    "jira_api": "http://jira.github.com/rest/api/2/",
    "jira_author_name": "Bob",
    "jira_remotelink":"/remotelink",
    "swarm_server":"http://swarmserver.github.com.com",
    "swarm_activity": "/api/v5/activity?max=100",
    "swarm_user_stream": "&stream=user-bob",
    "swarm_username": "bob",
    "swarm_password": "123456",
    "swarm_jira_start": 1
}
````
## Usage
 Update user Jira’s with Swarm changes
````
$ python main.py -u 
````
or
````
$ python main.py --user
````

or
````
$ python main.py
````

 Update all Jira’s with Swarm changes
 Warning: This will update all tickets in range with associated Swarm changes!!!
````
$ python main.py -a 
````
or
````
$ python main.py --all
````

## Options

**\-u**, **\-\-user**  
(Optional) Update Jira’s with user Swarm changes

**\-a**, **\-\-all**  
(Optional) Update Jira’s all Swarm changes

**\-h**, **\-\-help**  
(Optional) displays help

## License

MIT License

Copyright (c) 2017 Daniel Franklin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
