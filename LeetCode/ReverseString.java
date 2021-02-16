/*
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
*/

class Solution 
{
    public void reverseString(char[] s) 
    {
        // Make use of two pointers starting from the front and the back of the string
        // Loop through to iterate through the string

        int i = 0;
        int j = s.length;

        while (i < j)
        {
            s[i] = s[j];
            s[j] = s[i];
            
            i++;
            j--;
        
        }
    }
}