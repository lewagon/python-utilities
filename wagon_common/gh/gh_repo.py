
class GhRepo:
    """
    helper class for gh api commands
    """

    def __init__(self, name, is_org=True, verbose=False):

        self.is_org = is_org
        self.name = name
        self.verbose = verbose

        self.owner, self.repository = self.__identify(name)

    def __identify(self, name):
        """
        identify owner and repository from provided name
        (gh cli nomenclatura)
        """

        parts = name.split("/", maxsplit=1)

        if len(parts) == 2:
            owner = parts[0]
            repository = parts[1]
        else:
            owner = "lewagon"
            repository = parts[0]

        return owner, repository
