class GitHubRepo:
    """A class used to represent a single GitHub Repository"""

    def __init__(self, name, language, num_stars) -> None:
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self) -> str:
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars"

    def __repr__(self) -> str:
        return f"GitHubRepo({self.name}, {self.language}, {self.num_stars})"
