from hw.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Genre).get(uid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data_in):
        obj = Genre(**data_in)
        self.session.add(obj)
        self.session.commit()
        return obj

    def delete(self, rid):
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, data_in):
        obj = self.get_one(data_in.get('id'))
        if obj:
            if data_in.get('name'):
                obj.name = data_in.get('name')
            self.session.add(obj)
            self.session.commit()
            return obj
        return None
