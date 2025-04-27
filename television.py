class Television:
    """A class to represent a Television with basic functionality such as power, mute, channel, and volume control."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the Television with default power off, not muted, minimum volume, and minimum channel."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the television."""
        self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel by one if the television is on. Wrap around if the maximum channel is exceeded."""
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the channel by one if the television is on. Wrap around if below the minimum channel."""
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by one if the television is on, without exceeding the maximum volume."""
        if self.__status:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """Decrease the volume by one if the television is on, without going below the minimum volume."""
        if self.__status:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """Return a string representation of the television's current status."""
        return f'Power={self.__status}, Channel={self.__channel}, Volume={self.__volume}'