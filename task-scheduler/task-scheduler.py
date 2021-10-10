class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        max_freq = 0
        max_freq_task = None
        for task in tasks:
            if task not in task_counts:
                task_counts[task] = 0
            task_counts[task] += 1
            if task_counts[task] > max_freq:
                max_freq = task_counts[task]
                max_freq_task = task
        
        idle_time = (max_freq - 1) * n
        for task, count in task_counts.items():
            if task == max_freq_task:
                continue
            
            idle_time -= min(count, max_freq - 1)
        
        idle_time = max(idle_time, 0)
        
        return idle_time + len(tasks)
            