from smolagents.agents import CodeAgent

class EmailAgent(CodeAgent):
    def __init__(self, tools, model):
        """
        Initializes the EmailAgent with a list of tools and a model instance.
        Args:
            tools (list): List of Tool instances (e.g. [WriteEmail(), SendEmail()])
            model (object): A model instance with a .generate() method (not a string)
        """
        super().__init__(tools=tools, model=model)

    def run(self, user_input):
        """
        Handles user input and passes it to the CodeAgent's run method.
        """
        return super().run(user_input)
