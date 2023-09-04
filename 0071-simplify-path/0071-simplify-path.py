class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_stack = []
        
        path=path.split('/')
        print(path)
        for ele in path:
            
            if ele == '..':
                if path_stack:
                    path_stack.pop()
                continue
                
            if ele =='.':
                continue
            if ele =='':
                continue 
                
            else:
                path_stack.append(ele)
            
        return '/'+"/".join(path_stack)
            
        
        
        
 
            
            
        