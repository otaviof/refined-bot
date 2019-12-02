import pytest

from .jira import JiraClient

ISSUE_ID = 'BOT-1'


def __jiraClient() -> JiraClient:
    return JiraClient(
        server='http://jira.localtest.me:8080',
        basicAuth=('admin', '1'),
        storyPointsField='customfield_10000',
    )


def test_JiraClient_issue():
    jiraClient = __jiraClient()

    issue = jiraClient.issue(ISSUE_ID)

    assert issue.issueId == ISSUE_ID
    assert issue.summary != None
    assert issue.storyPoints > 0


def test_JiraClient_issuesWithoutStoryPoints():
    jiraClient = __jiraClient()
    issues = jiraClient.issuesWithoutStoryPoints()

    assert len(issues) == 1
