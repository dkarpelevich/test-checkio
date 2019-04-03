from typing import List


class Text:
    def __init__(self):
        self.text = ""
        self.font_name = ""

    def write(self, new_text):
        self.text += new_text

    def set_font(self, font_name):
        self.font_name = font_name

    def show(self):
        if self.font_name == "":
            return self.text
        else:
            return "[" + self.font_name + "]" + self.text + "[" + self.font_name + "]"

    def restore(self, saved_text: List):
        self.text = saved_text[0]
        self.font_name = saved_text[1]


class SavedText:
    def __init__(self):
        self._versions_dict = {}
        self._version = 0

    def save_text(self, text_object: Text):
        self._versions_dict.update({self._version: [text_object.text, text_object.font_name]})
        self._version += 1

    def get_version(self, version_number) -> List:
        return self._versions_dict[version_number]

if __name__ == '__main__':
    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
