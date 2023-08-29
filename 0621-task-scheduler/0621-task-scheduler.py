class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        no_units_tasks=[0]*26
        
        for letter in tasks:
            no_units_tasks[ord(letter)-ord('A')]+=1
            
        max_task = max(no_units_tasks)
        max_occurance = no_units_tasks.count(max_task)
        
        m = (max_task-1)*(n+1) + max_occurance
        n = len(tasks)
        return max(m,n)
            
         
    
                
        
        
        
        
        
        
        
        