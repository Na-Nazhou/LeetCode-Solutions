class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_distance(pt):
            return sqrt(pt[0] ** 2 + pt[1] ** 2)
    
        def quick_select(i, j, k):
            if i == j:
                return
            pivot_idx = partition(i, j)
            if pivot_idx == k:
                return
            
            if pivot_idx < k:
                return quick_select(pivot_idx + 1, j, k)
            else:
                return quick_select(i, pivot_idx - 1, k)
        
        def partition(i, j):
            pivot_idx = random.randint(i, j)
            swap(i, pivot_idx)
            ptr = i # last index <= pivot
            pivot = get_distance(points[i])
            for idx in range(i + 1, j + 1):
                if get_distance(points[idx]) <= pivot:
                    ptr += 1
                    swap(idx, ptr)
            swap(i, ptr)
            
            return ptr
                    
        
        def swap(i, j):
            points[i], points[j] = points[j], points[i]
            
        quick_select(0, len(points) - 1, k - 1)
        return points[:k]