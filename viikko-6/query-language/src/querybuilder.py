from matchers import All, Or, And, HasAtLeast, PlaysIn, HasFewerThan

# Pinorakentajan hengessä tämä ;)
class QueryBuilder:
    def __init__(self, matcher=All):
        self._matcher = matcher

    def playsIn (self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def hasAtLeast (self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def hasFewerThan (self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))
    
    def build(self):
        m = self._matcher
        self._matcher = All
        return m