class interview
{
    public static void main(String[] args)
    {
        // return the number of ways to represent long as a sum of two or more consecutive longs
        // e.g. 3 = 1 + 2, 4 = 1 + 1 + 1 + 1, 5 = 1 + 2 + 1, 6 = 1 + 1 + 2 + 1, 7 = 1 + 1 + 1 + 2 + 1
        // return 2
        int n = 7;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++)
        {
            nums[i] = i + 1;
        }
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                int sum = 0;
                for (int k = i; k <= j; k++)
                {
                    sum += nums[k];
                }
                if (sum == n)
                {
                    count++;
                }
            }
        }
        System.out.println(count);

    }
}