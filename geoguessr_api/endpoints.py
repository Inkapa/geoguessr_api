class API:
    def __init__(self, version: int = 3):
        self.BASE = f"https://www.geoguessr.com/api/v{version}"
        self.BASEV4 = f"https://www.geoguessr.com/api/v4" # Waiting for main version to go to 4

        self.ACCOUNTS = "/accounts"
        self.PROFILES = "/profiles"

        self.SIGNIN = self.BASE + self.ACCOUNTS + "/signin"
        self.ME = self.BASE + self.PROFILES + "/me"
