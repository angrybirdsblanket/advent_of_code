namespace Advent_Of_code {
  class day1a {
     public static async Task run() {
      int sum = 0;
      await foreach (string line in Program.readFile("../data/2023/day1.txt")) {
        int line_sum = calculateLine(line);
        sum += line_sum;
      }
      Console.WriteLine($"The sum of all the lines is {sum}");
    }
    static int calculateLine(string line) {
      int int1 = 0;
      int int2 = 0;
      foreach (char character in line) {
        try {

         if (int1 == 0) {
           int1 = Int32.Parse(character.ToString());
         }

         else {
           int2 = Int32.Parse(character.ToString());
         }

        }

        catch(System.FormatException) {
          continue;
        }

      }
      if(int1 == 0) return 0;
  
      else if (int2 == 0) {
        return Convert.ToInt32(Convert.ToString(int1) + Convert.ToString(int1));
      }

      return Convert.ToInt32(Convert.ToString(int1) + Convert.ToString(int2));
    } 
  }
}
