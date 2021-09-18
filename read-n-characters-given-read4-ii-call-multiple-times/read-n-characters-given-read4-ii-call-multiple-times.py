# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.temp = [0] * 4
        self.ptr = 0
        self.len = 0
        
    def read(self, buf: List[str], n: int) -> int:
        curr = 0
        
        while curr < n:
            # Consume existing buffer
            while curr < n and self.ptr < self.len:
                buf[curr] = self.temp[self.ptr]
                self.ptr += 1
                curr += 1
            
            if curr < n:
                # Read in new buffer
                self.ptr = 0
                self.len = 0
                self.len = read4(self.temp)

                # Stop reading if reaching eof
                if self.len == 0:
                    break
        
        return curr