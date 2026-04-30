from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol


class Mode(str, Enum):
    AM = "am"
    FM = "fm"
    USB = "usb"
    LSB = "lsb"
    CW = "cw"


class AudioStream(Protocol):
    def read(self):
        return


class Receiver(ABC):
    @abstractmethod
    def set_mode(self, mode: Mode):
        raise NotImplementedError

    @abstractmethod
    def set_frequency(self, frequency: int):
        raise NotImplementedError

    @abstractmethod
    def set_filter(self, lower_bound: int, upper_bound: int):
        raise NotImplementedError

    @abstractmethod
    def audioStream(self) -> AudioStream:
        raise NotImplementedError
