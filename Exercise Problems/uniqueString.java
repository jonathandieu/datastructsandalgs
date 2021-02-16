public class uniqueString
import java.util.*;

{
    // Take in a string and check whether or not every character is unique
    // If there is a duplicate char, return false
    // Else, return true
    public static void main(String[] args) 
    {
        return;
    }

    public boolean isUnique(String s)
    {
        // How to check whether one character is different than another
        // "abcd"
        array<boolean> myArr[] = new array<boolean>(false);

        if (s.length() > 128)
        {
        return false;
        }

        for (int i = 0; i < s.length(); i++)
        {
            // If it already exists in the array
            if (myArr[s.charAt(i)])
            {
                return false;
            }
            
            // If it doesn't exist;
            myArr[s.charAt(i)] = true; 
        }
        return true;
    }
}
