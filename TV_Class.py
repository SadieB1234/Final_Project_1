class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self, status = False, muted = False, volume = min_volume, channel = min_channel):

        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self): #used to turn tv on and off via status variable
        if self.__status == True:
            self.__status = False

        else:
            self.__status = True

    def mute(self): #used to mute and unmute via muted variable
        if self.__status:
            if self.__muted:
                self.__muted = False

            else:
                self.__muted = True


    def channel_up(self): #increase channel value when tv is on, if at max goes to min,
        if self.__status:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1

    def channel_down(self): #decrease channel value when tv is on, if on min goes to max
        if self.__status:
            if self.__channel == Television.min_channel:
                self.__channel = Television.max_channel
            else:
                self.__channel -= 1

    def volume_up(self): #increase vol when tv is on, if max stays at max
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume == Television.max_volume:
                pass
            else:
                self.__volume += 1

    def volume_down(self): #decrease vol when tv on, if min stays at min
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == Television.min_volume:
                pass
            else:
                self.__volume -= 1


    def __str__(self): #sends status in form of "TV status: Power = [status]. Channel = [channel], Volume = [volume]"
        return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.min_volume if self.__muted else self.__volume}'
