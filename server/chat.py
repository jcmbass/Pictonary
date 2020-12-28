"""
Represents and stores information about the chat
"""

class Chat(object):

    """Chat class for server side. Implements some usefull funcionalitty"""

    def __init__(self, r):
        """
        Instantiate chat without content
        :r: int
        :returns: None
        """
        self.content = []
        self.round = r

    def update_chat(self, msg):
        """
        Append string to the chat content.
        :msg: str
        :returns: None
        """
        self.content.append(msg)

    def get_chat(self):
        """
        :returns: [str]
        """
        return self.content

    def __len__(self):
        """
        :returns: int
        """
        return len(self.content)

    def __str__(self):
        """
        Content in a unique string.
        :returns: str
        """
        return "".join(self.content)

    def __repr__(self):
        """
        Object chat in string format
        :returns: str
        """
        return str(self)
