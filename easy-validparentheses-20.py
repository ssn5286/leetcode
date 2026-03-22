class Solution:
    def isValid(self, s: str) -> bool:
        staticDict = {'(': ')', '{': '}', '[' : ']'}
        stack = []
        
        for char in s:
            if char in staticDict:
                stack.append(char)
                continue
            if stack == [] or char != staticDict[stack.pop()]:
                return False

        return True if stack == [] else False

# “I use a stack to track opening brackets.
# When I see an opening bracket, I push it onto the stack.
# When I see a closing bracket, I check if it matches the top of the stack.
# If it doesn’t match or the stack is empty, I return false.
# At the end, if the stack is empty, the string is valid.
# This runs in O(n) time and O(n) space.”



        # tempDict = defaultdict(str)
        # tempDict ={'{':'}','[':']','(':')'}
        # tempList = []
        
        # for char in s:
        #     if char in tempDict:
        #        tempList.append(char)                         
        #     else:
        #         if tempList == [] or (tempDict[tempList.pop()] != char):
        #             return False

        # return True if tempList == [] else False
