class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr_dir = []
        path += "/"
        for c in path:
            if c != "/":
                curr_dir.append(c)
                continue
            
            if not curr_dir:
                continue
            
            if curr_dir == ["."]:
                curr_dir = []
                continue
                
            if curr_dir == [".", "."]:
                curr_dir = []
                if stack:
                    stack.pop()
                continue

            stack.append(curr_dir)
            curr_dir = []
        
        return "/" + "/".join(["".join(name) for name in stack])
            
        