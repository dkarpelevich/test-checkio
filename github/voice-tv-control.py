class VoiceCommand:
    def __init__(self, collection: list):
        self._collection = collection
        self._cursor = 0
        self._error = IndexError

    def first_channel(self):
        if len(self._collection) >= self._cursor + 1:
            self._cursor = 0
            return self._collection[self._cursor]
        self._raise_key_exception()

    def next_channel(self):
        if len(self._collection) >= self._cursor + 1:
            if self._cursor == len(self._collection) - 1:
                self._cursor = 0
            else:
                self._cursor += 1
            return self._collection[self._cursor]
        self._raise_key_exception()

    def last_channel(self):
        if len(self._collection) >= self._cursor + 1:
            self._cursor = len(self._collection) - 1
            return self._collection[self._cursor]
        self._raise_key_exception()

    def turn_channel(self, number):
        if self._cursor <= len(self._collection):
            self._cursor = number - 1
            return self._collection[self._cursor]
        self._raise_key_exception()

    def previous_channel(self):
        if len(self._collection) >= self._cursor + 1:
            if self._cursor == 0:
                self._cursor = len(self._collection) - 1
            else:
                self._cursor -= 1
            return self._collection[self._cursor]
        self._raise_key_exception()

    def current_channel(self):
        if self._cursor < len(self._collection):
            return self._collection[self._cursor]
        self._raise_key_exception()

    def is_exist(self, number_or_name):
        if isinstance(number_or_name, int):
            return 'Yes' if 1 <= number_or_name <= len(self._collection) else 'No'
        else:
            return 'Yes' if number_or_name in self._collection else 'No'

    def _raise_key_exception(self):
        raise self._error('Collection of class {} does not have key "{}"'.format(
            self.__class__.__name__, self._cursor))


if __name__ == '__main__':
    CHANNELS = ['BBC', 'Discovery', 'TV1000']
    controller = VoiceCommand(CHANNELS)
    controller.turn_channel(3)
    controller.next_channel()
    controller.current_channel()
