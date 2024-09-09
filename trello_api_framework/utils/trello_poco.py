class CreateCard:
    def __init__(self, name, desc, idList):
        self.name = name
        self.desc = desc
        self.idList = idList


class UpdateCard:
    def __init__(self, name, idList):
        self.name = name
        self.idList = idList


class CardResponse:
    def __init__(self, id, name, desc, id_list):
        self.id = id
        self.name = name
        self.desc = desc
        self.id_list = id_list
