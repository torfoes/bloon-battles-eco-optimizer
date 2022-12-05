class Bloon:

    def __init__(self, bloon_id, kwargs):
        self.type = bloon_id

        self.regrow = kwargs.get("regrow", False)
        self.camo = kwargs.get("camo", False)
        self.fortified = kwargs.get("fortified", False)


