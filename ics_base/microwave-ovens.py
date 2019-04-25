from abc import abstractmethod


class MicrowaveBase:
    def __init__(self):
        self.time = '00:00'

    @abstractmethod
    def show(self):
        pass


class Microwave1(MicrowaveBase):
    def show(self):
        self.time = '_' + self.time[1:]
        return self.time

class Microwave2(MicrowaveBase):
    def show(self):
        self.time = self.time[:len(self.time)-1] + '_'
        return self.time

class Microwave3(MicrowaveBase):
    def show(self):
        return self.time


class RemoteControl:
    def __init__(self, microwave):
        self.__microwave = microwave
        self.microwave_seconds = 0
        self.time_in_seconds = 0

    def show_time(self):
        return self.__microwave.show()

    def set_time(self, time):
        self.__microwave.time = time
        minute, sec = self.__microwave.time.split(':')
        self.microwave_seconds = int(minute) * 60 + int(sec)

    def add_time(self, time):
        self.time_in_seconds = (int(time[:time.rindex('s')]) if time.endswith('s')
                                else int(time[:time.rindex('m')])*60)

        add_minutes = (self.microwave_seconds + self.time_in_seconds) // 60
        add_seconds = (self.microwave_seconds + self.time_in_seconds) - 60 * add_minutes
        if self.microwave_seconds + self.time_in_seconds >= 5400:
            self.__microwave.time = '90:00'
        else:
            self.__microwave.time = '{0}:{1}'.format(str("{:02d}".format(add_minutes)),
                                                     str("{:02d}".format(add_seconds)))

    def del_time(self, time):
        self.time_in_seconds = (int(time[:time.rindex('s')]) if time.endswith('s')
                                else int(time[:time.rindex('m')]) * 60)

        decrease_minutes = (self.microwave_seconds - self.time_in_seconds) // 60
        decrease_seconds = (self.microwave_seconds - self.time_in_seconds) - 60 * decrease_minutes
        if self.microwave_seconds - self.time_in_seconds <= 0:
            self.__microwave.time = '00:00'
        else:
            self.__microwave.time = '{0}:{1}'.format(str("{:02d}".format(decrease_minutes)),
                                                     str("{:02d}".format(decrease_seconds)))


if __name__ == '__main__':
    microwave_1 = Microwave1()
    rc_1 = RemoteControl(microwave_1)
    rc_1.set_time("05:33")
    rc_1.del_time("30s")
    rc_1.del_time("2m")
    rc_1.show_time()