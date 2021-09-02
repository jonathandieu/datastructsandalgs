class IsWeird
{

    private static boolean isWeird(int n)
    {
        // Check if odd
        if (n % 2 != 0)
            return true;
        // Check if greater than 20 (and even)
        else if (n > 20 && (n % 2 == 0))
            return false;
        // Check if n is in range 2,5
        else if (n >= 2 && n <= 5 && (n % 2 == 0))
            return false;
        // Check if n is in range 2,5
        else if (n >= 6 && n <= 20 && (n % 2 == 0))
            return true;

        else
            return true;

    }

}
