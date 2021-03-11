class Item:

    def __init__(self, id, name, status = 'To Do', description = ''):
        self.id = id
        self.name = name
        self.status = status
        self.description = description

    @classmethod
    def fromTrelloCard(cls, card, list):
        return cls(card['id'], card['name'], list['name'])
