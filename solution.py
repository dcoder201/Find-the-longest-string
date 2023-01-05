#User function Template for python3


class Solution():
    def longestString(self, arr, n):
        #your code goes here
        s = set(arr)
        arr.sort(key=lambda x: (-len(x), x))
        for x in arr:
            for i in range(1, len(x)):
                if x[:i] not in s:
                    break
            else:
                return x
        return ""


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends
