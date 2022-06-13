class StructObj:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self):
        return "<StructObj: %s>" % self.__dict__