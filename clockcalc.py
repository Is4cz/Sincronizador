class Strtime:
          def __init__(self, format, milli = 0):
                    """Just __init__."""
                    self.hour = int(format.split(':')[0])
                    self.minute = int(format.split(':')[1])
                    self.seconds = float(format.split(':')[2])
                    self.milliseconds = float(milli)
          def decreaseOtherTime(self, otherTime: 'Strtime') -> str:
                    """It can subtract two different times by converting them to milliseconds and then returning normally."""
                    # Setting the schedules
                    totalMilliVideo = otherTime.sumsAllValues() # Video
                    totalMilliDate = self.sumsAllValues() # Data
                    # Subtracting the times
                    difference = totalMilliDate - totalMilliVideo
                    # Adding 24 hours if the difference is negative
                    i = 0
                    while difference < 0:
                              i += 1
                              difference += 24 * 3600 # 24 Hours * 3600 Seconds (1 Hour = 3600 Seconds)
                    # Calculating the result in hours, minutes, seconds and milliseconds
                    print('diferença: {}'.format(difference))
                    hourResult = int(difference // 3600) # We use the division integers and the remainder continues
                    rest = difference % 3600
                    minutesResult = int(rest // 60)
                    secondsResult = int(rest % 60)
                    milliResultinSeconds = int((rest - int(rest)) * 1000) / 1000 # Only God knows that
                    # Returning
                    return '{}:{}:{}'.format(hourResult, minutesResult, secondsResult), milliResultinSeconds
          def returnFormat(self) -> str:
                    """Just return all values in time format."""
                    return('{}:{}:{};{}'.format(self.hour, self.minute, self.seconds, self.milliseconds))
          def sumsAllValues(self) -> float:
                    """Adds all values, also converts them to seconds."""
                    return (self.hour * 3600) + (self.minute * 60) + self.seconds + (self.milliseconds / 1000)