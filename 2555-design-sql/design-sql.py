class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.res = defaultdict(dict)
        self.temp = defaultdict(int)
        self.col = defaultdict(int)


        for i in range(len(names)):
            self.temp[names[i]] = 0
            self.col[names[i]] = columns[i]
            

        #print(self.res)

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.col or len(row) != self.col[name]:
            return False
       
        self.temp[name] += 1
        self.res[name][self.temp[name]] = row
        return True
        
        
    def rmv(self, name: str, rowId: int) -> None:
        if rowId in self.res[name]:
            del self.res[name][rowId]
        

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name in self.res and rowId in self.res[name] and 0 <= columnId - 1 < self.col[name]:
            return self.res[name][rowId][columnId - 1]
        
        return "<null>"

    def exp(self, name: str) -> List[str]:
        ans = []
        for i in self.res[name]:
            ans.append(','.join([str(i)] + self.res[name][i]))
        
        return ans

# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)