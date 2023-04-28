from typing import Union

channels = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels: list) -> None:
        self.channels = channels
        self.current_channel = 0
        self.count_channels = len(self.channels)


    def first_channel(self) -> str:
        return self.channels[self.current_channel]


    def last_channel(self) -> str:
        return self.channels[self.count_channels - 1]


    def turn_channel(self, number_channel: int) -> str:
        return self.channels[number_channel - 1]


    def next_channel(self) -> str:
        self.current_channel = (self.current_channel + 1) % self.count_channels
        return self.channels[self.current_channel]


    def previous_channel(self) -> str:
        self.current_channel = (self.current_channel - 1) % self.count_channels
        return self.channels[self.current_channel]


    def current_channel_metod(self) -> str:
        return self.channels[self.current_channel]


    def is_exist(self, channel: Union[int, str]) -> str:
        if type(channel) is int:
            if 1 <= channel <= self.count_channels:
                return 'Yes'
            else:
                return 'No'
        else:
            if channel in self.channels:
                return 'Yes'
            else:
                return 'No'


controller = TVController(channels)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel_metod() == "BBC"

assert controller.is_exist(4) == "No"

assert controller.is_exist("BBC") == "Yes"