from jira_client import jira
from slack_client import slack


class Executor():
    jiraClient: jira.JiraClient = None
    slackClient: slack.SlackClient = None

    def __init__(self):
        pass
