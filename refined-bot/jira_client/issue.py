from jira.resources import Issue


class JiraIssue():
    """
        Internal representation of an Jira issue.
    """

    issue: Issue = None
    issueId: str = None
    summary: str = None
    storyPoints: int = None

    def __init__(self, issue: Issue, storyPointsField: str):
        """
            Building instance by copying Issue's attributes.
        """
        self.issue = issue
        self.issueId = issue.key
        self.summary = issue.fields.summary
        self.storyPoints = self.__extractField(issue.raw, storyPointsField)

    def __extractField(self, raw: dict, name: str):
        """
            Based on issue raw contents (issue.raw dictionary), search and extract field.
        """
        if not 'fields' in raw:
            return None
        fields = raw['fields']
        if not name in fields:
            return None
        return fields[name]
