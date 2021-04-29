import java.util.Arrays;

class fibonacci
{
    private static final int UNINITIALIZED = -1;

    public static void main(String[] args)
    {

        // int n = (args.length > 0) ? Integer.parseInt(args[0]) : 0;
        for (int n = 0; n <= 40; n++)
        {
            System.out.println("Fib(" + n + ") = " + fibRecurse(n));
            System.out.println("FibMemo(" + n + ") = " + fibMemo(n));
            System.out.println("FibDP(" + n + ") = " + fibDP(n));
            System.out.println("FibUltraDP(" + n + ") = " + fibUltraDP(n));
        }

    }

    // Naive recursive approach
    public static int fibRecurse(int n)
    {
        // Base cases
        if (n < 2)
            return n;
        else
        // Since Fibonacci is defined as the number before plus the last number:
            return fibRecurse(n - 1) + fibRecurse(n - 2);
    }

    // Memoization approach with recursion

    // Wrapper function
    public static int fibMemo(int n)
    {
        // Create memo to store recursive calls in
        // Size must be n + 1 since we want n as a valid index of the array
        int[] memo = new int[n + 1];

        // Fill the array with UNINITIALIZED values
        Arrays.fill(memo, UNINITIALIZED);

        // Calls the private function
        return fibMemo(n, memo);
    }

    // Driver function
    private static int fibMemo(int n, int[] memo)
    {
        // Original base case
        if (n < 2)
            return n;

        // New base case for memoization
        if (memo[n] != UNINITIALIZED)
            return memo[n];

        else
            return fibMemo(n - 1, memo) + fibMemo(n - 2, memo);


        }

        // Iterative Dynamic Programming approach that does not use
        // any recursion whatsoever, instead using a matrix to keep
        // track of the recursive calls by eliminating recursion
        // Bottom up
        public static int fibDP(int n)
    {
        // Original base case which also prevents us from an indexoutofbounds
        // exception when using 0
        if (n < 2)
            return n;
        // Create a new matrix once again with size n + 1 as we want n as
        // a valid index - also ensure that array is at least size 2
        int[] matrix = new int[Math.max(2, n + 1)];

        // Initialize the matrix initial conds. for the bottom-up approach
        matrix[0] = 0;
        matrix[1] = 1;

        // This loop starts at 2 because the first two indices were already
        // initialized, and we are filling them up one by one.
        for (int i = 2; i <= n; i++)
            matrix[i] = matrix[i - 1] + matrix[i - 2];

        return matrix[n];
    }

    public static int fibUltraDP(int n)
    {
        // We can just create an array of size 2 and overwrite as we go
        int[] matrix = new int[2];

        // Initialize values just like before
        matrix[0] = 0;
        matrix[1] = 1;

        // Set up the loop like before with i starting at 2
        for (int i = 2; i <= n; i++)
            // Use the mod trick
            matrix[i % 2] = matrix[(i - 1) % 2] + matrix[(i - 2) % 2];

        // Return the index of the array where n % 2
        return matrix[n % 2];
    }

}
