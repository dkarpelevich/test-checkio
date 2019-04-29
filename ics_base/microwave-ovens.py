from abc import abstractmethod

class MicrowaveBase:
    def __init__(self):
        self.time = '00:00'

    @abstractmethod
    def show(self):
        pass


class Microwave1(MicrowaveBase):
    def show(self):
        self.time = '{0}{1}'.format('_', self.time[1:])
        return self.time


class Microwave2(MicrowaveBase):
    def show(self):
        self.time = '{0}{1}'.format(self.time[:len(self.time) - 1], '_')
        return self.time


class Microwave3(MicrowaveBase):
    def show(self):
        return self.time


class RemoteControl:
    def __init__(self, microwave: MicrowaveBase):
        self.__microwave = microwave
        self.__time_on_microwave_seconds = 0
        self.__time_in_seconds = 0

    def show_time(self):
        m, s = divmod(self.__time_on_microwave_seconds, 60)
        self.__microwave.time = str('{:02d}:{:02d}'.format(m, s))
        return self.__microwave.show()

    def set_time(self, time: str):
        self.__microwave.time = time
        minute, sec = [int(i) for i in self.__microwave.time.split(':')]
        self.__time_on_microwave_seconds = minute * 60 + sec

    @staticmethod
    def convert_time_to_seconds(time: str):
        return (int(time[:time.rindex('s')]) if time.endswith('s')
                else int(time[:time.rindex('m')]) * 60)

    def add_time(self, time: str):
        self.__time_in_seconds = RemoteControl.convert_time_to_seconds(time)
        self.__time_on_microwave_seconds = self.__time_on_microwave_seconds + self.__time_in_seconds
        if self.__time_on_microwave_seconds >= 5400:
            self.__time_on_microwave_seconds = 5400

    def del_time(self, time: str):
        self.__time_in_seconds = RemoteControl.convert_time_to_seconds(time)
        self.__time_on_microwave_seconds = self.__time_on_microwave_seconds - self.__time_in_seconds
        if self.__time_on_microwave_seconds <= 0:
            self.__time_on_microwave_seconds = 0


if __name__ == '__main__':
    microwave_2 = Microwave2()
    rc_2 = RemoteControl(microwave_2)
    rc_2.set_time("89:00")
    rc_2.add_time("90s")
    rc_2.add_time("20m")
    rc_2.show_time()
