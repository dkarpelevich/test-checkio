from abc import ABC


class Observable(ABC):

    def __init__(self):
        self.observers = []
        self.person_place_dict = {}

    def add_friend(self, observer) -> None:
        self.observers.append(observer)

    def del_friend(self, observer) -> None:
        try:
            self.observers.remove(observer)
        except ValueError:
            print('There is no such person invited')

    def send_invites(self, message: str) -> None:
        for observer in self.observers:
            self.person_place_dict.update({observer: message})


class Party(Observable):
    def __init__(self, place):
        super().__init__()
        self.place = place

    def getter(self):
        print(self.place)

class Friend(Party):
    def __init__(self, name, place):
        super().__init__(place)
        self.name = name

    def show_invite(self):
        # print(self.place.person_place_dict)
        # self.place.getter()
        try:
            print(str(self.place.place) + ': ' + str(self.place.person_place_dict[self]))
            return str(self.place.place) + ': ' + str(self.place.person_place_dict[self])
        except KeyError:
            print('No party...')
            return 'No party...'


if __name__ == '__main__':
    party = Party("Midnight Pub")
    nick = Friend("Nick", party)
    john = Friend("John", party)
    lucy = Friend("Lucy", party)
    chuck = Friend("Chuck", party)

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
