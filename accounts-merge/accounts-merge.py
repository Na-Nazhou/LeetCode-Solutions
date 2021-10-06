class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(list)
        email_name_map = {}
        
        for account in accounts:
            name = account[0]
            email = account[1]
            email_name_map[email] = name
            
            for i in range(2, len(account)):
                other_email = account[i]
                email_name_map[other_email] = name
                
                adj_list[email].append(other_email)
                adj_list[other_email].append(email)
        
        visited = set()
        
        def dfs(email, group):
            visited.add(email)
            group.append(email)
            
            for other_email in adj_list[email]:
                if other_email not in visited:
                    dfs(other_email, group)
        
        ans = []
        for email, name in email_name_map.items():
            if email not in visited:
                group = []
                dfs(email, group)
                group.sort()
                ans.append([name] + group)
        
        return ans