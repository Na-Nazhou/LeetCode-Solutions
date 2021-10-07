class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []
        for component in components:
            if not component:
                continue
            
            if component == ".":
                continue
            
            if component == "..":
                if stack:
                    stack.pop()
                continue
            
            stack.append(component)
        
        return "/" + "/".join(stack)