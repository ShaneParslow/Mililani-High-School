class DataPoint:

    def __init__(self, timestamp, kilowatts):#store timeStamp as a unix timestamp
        self.date = date
        self.timestamp = timestamp
        self.kilowatts = kilowatts


class Building:

    def __init__(self, name, dataPoints):
        self.name = name
        self.dataPoints = dataPoints


class Campus:

    def __init__(self, name, buildings):
        self.name = name
        self.buildings = buildings