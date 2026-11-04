class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] >= newInterval[0]:
                left = min(interval[0], newInterval[0])
                right = newInterval[1]
                for j in range(i, len(intervals)):
                    _interval = intervals[j]
                    if right > _interval[1]:
                        continue
                    elif right < _interval[0]:
                        break
                    elif right >= _interval[0]:
                        right = max(_interval[1], right)
                        # res.append([left, right])
                        break
                res.append([left, right])
                if right < _interval[0]:
                    # res.append([left, right])
                    res.append(_interval)
                for k in range(j+1, len(intervals)):
                    res.append(intervals[k])
                
                return res
                                
            res.append(interval)
    
        res.append(newInterval)

        return res
            