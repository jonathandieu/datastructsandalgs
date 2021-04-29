class fibonacci
{
    public static void main(String[] args)
    {
        System.out.println(fibRecurse(10));

    }

    // Naive recursive approach
    public static int fibRecurse(int n)
    {
        // Base cases
        if (n < 2)
            return n;
        else
            return fib(n - 1) + n;
    }

    public static int fibMemo(int n)
    {

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
