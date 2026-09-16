class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack.pop()
                temperatures[top] = i - top
            stack.append(i)

        while stack:
            temperatures[stack.pop()] = 0
            
        return temperatures


                
