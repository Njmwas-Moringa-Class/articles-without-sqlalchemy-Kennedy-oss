class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author  # Instance of Author
        self._magazine = magazine  # Instance of Magazine
        self._title = title
        Article._all_articles.append(self)
        author._articles.append(self)  # Ensure article is associated with the author upon instantiation

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls._all_articles

