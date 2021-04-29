class fibonacci
{
    public static void main(String[] args)
    {
        System.out.println(fibRecurse(9));
        System.out.println(fibMemo(9));
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
        int[] memo = new int[n];

        // Calls the private function
        return fibMemo(n, memo);
    }

    // Driver function
    private static int fibMemo(int n, int[] memo)
    {
        if (n < 2)
            return n;
        else
            return fibMemo(n - 1, memo) + fibMemo(n - 2, memo);

        // Initialize the memo

    }

    // Iterative Dynamic Programming approach that does not use
    // any recursion whatsoever, instead using a matrix to keep
    // track of the recursive calls
    public static int fibDP(int n)
    {
        // Create a new matrix
        int[] matrix = new int[n];


    }
}
