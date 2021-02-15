/*
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
*/
import java.util.*;
class Solution 
{
    public boolean canConstruct(String ransomNote, String magazine) 
    {
        // Instantiate a new HashMap
            // We use this because we want to keep track of the number of letters we have

        HashMap<Character, Integer> counter = new HashMap<>();

        // Enhanced For-Loop iterating over each character in the character array
        // This populates the hashmap with our values
        for (char c : magazine.toCharArray())
        {
            // As we iterate over the char array, we put the character and map it to an integer count.
            // the second argument uses getOrDefault
                // This returns the value mapped with the specified key, otherwise zero is returned.
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }

        for (char c : ransomNote.toCharArray())
        {
            // If we go through and see that our hashmap doesn't have the value in it or the count of that particular letter is not enough, (we don't have enough letters to build note)
            if (!counter.containsKey(c) || counter.get(c) <= 0)
            {
                return false;
            }
            counter.put(c, counter.get(c) - 1); // Not sure what this does
            
        } 
        return true;
    }
}