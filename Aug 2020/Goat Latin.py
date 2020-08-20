class Solution:
    def toGoatLatin(self, S: str) -> str:
        arr = S.split(' ')
        for i in range(len(arr)):
            if arr[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                arr[i] = arr[i]
            else:
                arr[i] = arr[i][1:] + arr[i][0]
            arr[i] += 'ma' + "".join(['a' for _ in range(i + 1)])
        return " ".join(arr)



s = "I speak Goat Latin"
print(Solution().toGoatLatin(s))