class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(g, visited, root, ls):
            if root in visited:
                return
            
            visited.add(root)
            ls.append(root)
            
            for linked_email in g[root]:
                dfs(g, visited, linked_email, ls)
        
        g = defaultdict(list)
        m = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in g:
                g[first_email] = []
            if first_email not in m:
                m[first_email] = name
            for i in range(2, len(account)):
                other_email = account[i]
                g[first_email].append(other_email)
                g[other_email].append(first_email)
        
        visited = set()
        ans = []
        for email in g.keys():
            if email not in visited:
                linked_emails = []
                dfs(g, visited, email, linked_emails)
                linked_emails.sort()
                account = [m[email]]
                account += linked_emails
                ans.append(account)
                
        return ans
                
                