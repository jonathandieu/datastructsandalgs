import java.lang.* ;
import java.util.* ;

public class magicSquare
{
    public static void main(String[] args)
    {
        if (args.length == 1)
            makeMagicSquare(Integer.parseInt(args[0]));
        else
            makeMagicSquare(4);
    }

    public static void makeMagicSquare(int n)
    {
        // Magic Constant Formula
        int magicConstant = (int) (n * (Math.pow(n, 2) + 1) / 2);
        System.out.println("Magic Constant: " + magicConstant);

        // Instantiate new 2D matrix
        int[][] magicSquare = new int[n][n];

        // Initialize the matrix to 0
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                magicSquare[i][j] = 0;
                System.out.print(magicSquare[i][j] + " ");
            }
            System.out.println();
        }

        int num = 1;
        int i = 0;
        int j = (num / 2);

        while (num <= Math.pow(n, 2))
        {
            magicSquare[i][j] = num;
            num++;
            int i2 = (i - 1) % n;
            int j2 = (j + 1) % n;

            if (magicSquare[i2][j2] != 0)
                i++;
            else
            {
                i = i2;
                j = j2;
            }
        }

        System.out.println(Arrays.toString(magicSquare));
    }
}