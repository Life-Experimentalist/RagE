class Agent:
    def __init__(self, name: str):
        self.name = name

    def act(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class SimpleAgent(Agent):
    def act(self):
        return f"{self.name} is performing a simple action."

class ComplexAgent(Agent):
    def act(self):
        return f"{self.name} is performing a complex action with additional logic."

def create_agent(agent_type: str, name: str) -> Agent:
    if agent_type == "simple":
        return SimpleAgent(name)
    elif agent_type == "complex":
        return ComplexAgent(name)
    else:
        raise ValueError("Unknown agent type.")