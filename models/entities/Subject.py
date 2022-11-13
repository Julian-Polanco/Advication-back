class Subject():

    def __init__(self, id, name, description) -> None:
        self.id = id
        self.name = name
        self.description = description

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

#class SubjectJoin():
#
#    def __init__(self, name, descriptionShort, descriptionLarge, price, code, score, image) -> None:
#        self.name = name
#        self.descriptionShort = descriptionShort
#        self.descriptionLarge = descriptionLarge
#        self.price = price
#        self.code = code
#        self.score = score
#        self.image = image
#
#    def to_JSON(self):
#        return {
#            'name': self.name,
#            'descriptionShort': self.descriptionShort,
#            'descriptionLarge': self.descriptionLarge,
#            'price': self.price,
#            'code': self.code,
#            'score': self.score,
#            'image': self.image
#        }
