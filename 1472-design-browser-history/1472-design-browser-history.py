class DLLNode:
    def __init__(self, url: str):
        self.val = url
        self.prev, self.next = None, None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DLLNode(homepage)
        self.current = self.history
        

    def visit(self, url: str) -> None:
        node = DLLNode(url)
        self.current.next = node
        node.prev = self.current
        self.current = node

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -=1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            self.current = self.current.next
            steps -=1

        return self.current.val

            
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)