def Solution(s):
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        def longest_palindromic_curr(start, end):
            if start < 0 or end >= n:
                return 0 
            if s[start] != s[end]:
                return 0
            return 1 + longest_palindromic_curr(start-1, end+1)
        start = 0
        end = 0
        for i in range(n - 2):
            half_length = 0
            if s[i] == s[i+1]:
                half_length = max(half_length, longest_palindromic_curr(i, i+1))
            if s[i] == s[i+2]:
                half_length = max(half_length, longest_palindromic_curr(i+1, i+1))
            
            if half_length > (end - start)/2:
                start = i - half_length + 2
                end = i + half_length
            print(start, end)

        return s[start: end+1]
    
    return longestPalindrome(s)


s = "babad"
print(Solution(s))