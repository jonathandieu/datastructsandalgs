class Assessment
{
    public static int[] merge(int[] a, int[] b)
    {
        int[] c = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        while (i < a.length && j < b.length)
        {
            if (a[i] < b[j])
            {
                c[k] = a[i];
                i++;
            }
            else
            {
                c[k] = b[j];
                j++;
            }
            k++;
        }
        while (i < a.length)
        {
            c[k] = a[i];
            i++;
            k++;
        }
        while (j < b.length)
        {
            c[k] = b[j];
            j++;
            k++;
        }
        return c;
    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    public static int sumOfLeftLeaves(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return root.val;
        }
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
    }

    public static void main(String[] args)
    {
        System.out.println(test1() ? "Test 1: Passed" : "Test 1: Failed");
        System.out.println(test2() ? "Test 2: Passed" : "Test 2: Failed");
        System.out.println(test3() ? "Test 3: Passed" : "Test 3: Failed");
    }

    public static boolean test1()
    {
        return false;
    }

    public static boolean test2()
    {
        return false;
    }

    public static boolean test3()
    {
        return false;
    }
}