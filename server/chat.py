"""
Represents and stores information about the chat
"""

class Chat(object):

    """Docstring for chat. """

    def __init__(self, r):
        """TODO: to be defined. """
        self.content = []
        self.round = r

    def update_chat(self, msg):
        """TODO: Docstring for update_chat.

        :msg: TODO
        :returns: TODO

        """
        self.content.append(msg)

    def get_chat(self):
        """TODO: Docstring for get_chat.
        :returns: TODO

        """
        return self.content

    def __len__(self):
        """TODO: Docstring for __len__.
        :returns: TODO

        """
        return len(self.content)

    def __str__(self):
        """TODO: Docstring for __str__.
        :returns: TODO

        """
        return "".join(self.content)

    def __repr__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO

        """
        return str(self)
