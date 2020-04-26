class SearchFilter:
    keywords = []
    season = None # an array

    def __init__(self, query=None, season=None):
        if query is None:
            if query is None:
                self.keywords = []
        elif isinstance(query, str):
            if len(query) == 0:
                self.keywords = []
            else:
                query_split = query.split(" ")
                keywords = []
                for keyword in query_split:
                    keywords.append(keyword)
                self.keywords = keywords
        if season is None or isinstance(season, list):
            self.season = season
        else:
            raise TypeError("Season must be a string or NoneType.")

    def __set__(self, instance, value):
        raise AttributeError("Setting attribute is forbidden")
