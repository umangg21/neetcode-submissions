

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        need = len(set(t))
        s_window = Counter()
        t_window = Counter(t)
        left = 0
        res_left, res_right = -1, -1
        prev_window_size = float("inf")


        for right in range(len(s)):
            s_window[s[right]] += 1

            if s_window[s[right]] == t_window[s[right]]:
                have += 1

            # window is currently valid we want to shrink
            # and see what is the smallest size of the valid window is
            while have == need:
                if (right - left + 1) < prev_window_size:
                    res_left, res_right = left, right
                    prev_window_size = right - left + 1
                # start shrinking
                s_window[s[left]] -= 1

                if s_window[s[left]] < t_window[s[left]]:
                    have -= 1

                left += 1


        return s[res_left: res_right + 1] if res_left != -1 and res_right != -1 else ""