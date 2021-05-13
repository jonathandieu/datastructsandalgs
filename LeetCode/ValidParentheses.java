import java.util.Arrays;

public class ValidParentheses
{
    // Given a string s containing just the characters '(', ')', '{', '}', '[', and ']'
    // determine if the input string is valid

    public static boolean isValid(String s)
    {
        // String is valid if:
        // 1. Open brackets must be closed by the same type of brackets
        // 2. Open brackets must be closed in the right order

        char[] charray = s.toCharArray();
        System.out.println("Ok here we go: " + Arrays.toString(charray));

        return false;

    }

    public static void main(String[] args)
    {
        String s = "bruh";
        isValid(s);
    }
}
