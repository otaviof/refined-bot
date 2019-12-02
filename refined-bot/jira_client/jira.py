from typing import List

from jira import JIRA

from .issue import JiraIssue


class JiraClient():
    """
        Jira API client.
    """

    jira: JIRA = None
    storyPointsField: str = None

    def __init__(self, server: str, basicAuth: tuple, storyPointsField: str):
        """
            Instantiate API client with basic authentication.
        """
        self.jira = JIRA(options={'server': server}, basic_auth=basicAuth)
        self.storyPointsField = storyPointsField

    def issue(self, issueId: str) -> JiraIssue:
        """
            Issue retriever based on identifier, return as a local representation.
        """
        issue = self.jira.issue(issueId)
        return JiraIssue(issue=issue, storyPointsField=self.storyPointsField)

    def __emptyStoryPointsJQL(self) -> str:
        """
            Build JQL query to find issues without story points. In case of custom field it uses
            the identifier "cf" and field-id.
        """
        fieldId = self.storyPointsField
        if self.storyPointsField.startswith('customfield_'):
            fieldId = 'cf[%s]' % (self.storyPointsField.split('_')[1])
        return '\'%s\' is empty' % (fieldId)

    def issuesWithoutStoryPoints(self) -> List[JiraIssue]:
        """
            Using "search_issues" to return issues without story points.
        """
        jiraIssues = []
        for issue in self.jira.search_issues(jql_str=self.__emptyStoryPointsJQL()):
            jiraIssue = JiraIssue(issue, storyPointsField=self.storyPointsField)
            jiraIssues.append(jiraIssue)
        return jiraIssues
