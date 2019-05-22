VOWELS = "aeiou"

class Person:
    def __init__(self, name):
        self.name = name
        self.list_of_messages = []

    def send(self, message):
        self.list_of_messages.append(message)

class Chat:
    def __init__(self):
        self._human = None
        self._robot = None

    def connect_human(self, human):
        self._human = human

    def connect_robot(self, robot):
        self._robot = robot

    def show_human_dialogue(self):
        # Chat.show_dialogue(self._human, self._robot)
        dialogue = ''
        for i in range(len(self._human.list_of_messages)):
            dialogue += '{0} said: {1}\n{2} said: {3}\n'\
                .format(self._human.name, self._human.list_of_messages[i],
                        self._robot.name, self._robot.list_of_messages[i])
        return dialogue.rstrip()

    @staticmethod
    def prepare_robot_message(person):
        list_inverted_messages = []
        for i in range(len(person.list_of_messages)):
            inverted_message = person.list_of_messages[i].lower()
            for j in inverted_message:
                if j in VOWELS:
                    inverted_message = inverted_message.replace(j, '0')
                else:
                    inverted_message = inverted_message.replace(j, '1')
            list_inverted_messages.append(inverted_message)
        return list_inverted_messages

    def show_robot_dialogue(self):
        dialogue = ''
        list_human_messages = Chat.prepare_robot_message(self._human)
        list_robot_messages = Chat.prepare_robot_message(self._robot)
        for i in range(len(list_human_messages)):
            dialogue += '{0} said: {1}\n{2} said: {3}\n'\
                .format(self._human.name, list_human_messages[i],
                        self._robot.name, list_robot_messages[i])
        return dialogue.rstrip()

class Human(Person):
    pass

class Robot(Person):
    pass


if __name__ == '__main__':
    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""