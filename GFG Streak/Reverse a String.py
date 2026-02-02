class Solution:

    # Function to reverse a string in-place
    def reverseString(self, s: str) -> str:
        # Convert string to a list of characters
        char_list = list(s)
        n = len(char_list)

        # Loop to swap characters from start and end
        for i in range(n // 2):
            # Swapping characters
            char_list[i], char_list[n - i - 1] = char_list[n - i -
                                                           1], char_list[i]

        # Convert list back to string and return
        return ''.join(char_list)
