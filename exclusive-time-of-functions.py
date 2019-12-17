class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        def process_log(line):
            func_id, status, time = line.split(":")
            return int(func_id), status , int(time)

        from collections import defaultdict

        sys_stack = []
        time_counter = defaultdict(int)

        for log in logs:
            func_id, status, time = process_log(log)
            if status == "start":
                if not sys_stack:
                    pass
                else:
                    # suspend last func
                    last_func_id, last_func_st_time = sys_stack[-1]
                    time_counter[last_func_id] += time - last_func_st_time
                sys_stack.append([func_id, time])
            elif status == "end":
                last_func_id, last_func_st_time = sys_stack.pop()
                assert last_func_id == func_id
                time_counter[last_func_id] += time - last_func_st_time + 1
                if sys_stack:
                    sys_stack[-1][1] = time + 1
        return [time_counter[k] for k in sorted(time_counter.keys())]