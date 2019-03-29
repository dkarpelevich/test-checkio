class Friends:
    def __init__(self, connections):
        self.connections = [set(i) for i in {frozenset(i) for i in connections}]

    def add(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        else:
            return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        names_set = set()
        for connection in self.connections:
            for j in connection:
                names_set.add(j)
        return names_set

    def connected(self, name):
        connected_set = set()
        if name not in self.names():
            return set()
        for connection in self.connections:
                if name in connection:
                    connected_set.add(list(connection - {name})[0])
        return connected_set


if __name__ == '__main__':
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
