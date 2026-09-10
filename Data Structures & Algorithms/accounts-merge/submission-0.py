class Solution:
    class Disjoint:
        def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.rank = [0] * size

        def find(self, i):
            if self.parent[i] == i:
                return self.parent[i]
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        
        def Union(self, i, j):
            rootI = self.find(i)
            rootJ = self.find(j)

            if rootI == rootJ:
                return False
            
            if self.rank[rootI] > self.rank[rootJ]:
                self.parent[rootJ] = rootI  # 🔧 FIXED: rootJ was lowercase 'j'
            elif self.rank[rootI] < self.rank[rootJ]:
                self.parent[rootI] = rootJ
            else:
                self.parent[rootJ] = rootI
                self.rank[rootI] += 1
            return True

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dsu = self.Disjoint(n)
        emailToAcc = {}

        for accId, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    dsu.Union(accId, emailToAcc[email])
                else:
                    emailToAcc[email] = accId

        idToAcc = defaultdict(list)

        for email, accId in emailToAcc.items():
            rootId = dsu.find(accId)
            idToAcc[rootId].append(email)  
        
        res = []
        for root_id, emails in idToAcc.items():
            name = accounts[root_id][0]  
            res.append([name] + sorted(emails))
            
        return res