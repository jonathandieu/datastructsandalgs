class stringTimes
{
    public static void main(String[] args)
    {
        System.out.println(stringTime("yeet", 3));
    }

    public static String stringTime(String str, int n) {

      StringBuilder newString = new StringBuilder();
      for(int i = 0; i < n; i++)
      {
        newString.append(str);
      }
      return newString.toString();
    }

}
