class UndergroundSystem:

    def __init__(self):
        self.checkin_map  = {}
        self.average_time_map = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        '''
        just store the details in a map with key id
        '''
        
        self.checkin_map[id] = (stationName, t)
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        '''
        update the average time map
        - check if the tuple exists in the time map
            - yes : just add the time to total_time and increase total_trips by 1
            - no : add new key value
        '''
        end_station = stationName
        start_station = self.checkin_map[id][0]
        start_time = self.checkin_map[id][1]
        end_time = t
        total_time = end_time - start_time
        
        if (start_station, end_station) not in self.average_time_map:
            self.average_time_map[(start_station, end_station)] = (total_time, 1)
        else:
            old_total_time = self.average_time_map[(start_station, end_station)][0]
            old_total_trips = self.average_time_map[(start_station, end_station)][1]
            self.average_time_map[(start_station, end_station)] = (old_total_time + total_time, old_total_trips + 1)
        
        return
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_time_map[(startStation, endStation)][0]/ self.average_time_map[(startStation, endStation)][1]
    
    # stuff which needs to be stored
    '''
    id -> checkin location: time map
    
    as soon as a checkout is called 
    1. time map is looked  up for the card id
    2. (start, end) location tuple is updated with value (end_time - start_time) 
    but this is not the average. we need to find the average
        - map can be like this : (start, end) - (total_time, total_trips)
    
    '''


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)