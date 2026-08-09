class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
    
        min_heap = []
        current_passengers = 0
        
        for num_passengers, start, end in trips:
            
            # Drop off passengers whose destination is less than or equal to current start time
            while min_heap and min_heap[0][0] <= start:
                _, dropped_passengers = heapq.heappop(min_heap)
                current_passengers -= dropped_passengers
                
            # Pick up the new passengers
            heapq.heappush(min_heap, (end, num_passengers))
            current_passengers += num_passengers
            
            # If at any point the car is overloaded, return False
            if current_passengers > capacity:
                return False
                
        return True

