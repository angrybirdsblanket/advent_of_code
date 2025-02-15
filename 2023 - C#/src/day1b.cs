using System.Text.RegularExpressions;

namespace Advent_Of_code {

  class day1b {

    public static async Task run() {

      int sum = 0;

      await foreach (string line in Program.readFile("../data/2023/day1.txt")) {
        sum += calculateLine(line);
      }
      Console.WriteLine($"The final sum is {sum}");
    }
    static int calculateLine(string line) {
      int int1 = 0;
      int int2 = 0; 
      Dictionary<string, int> wordToDigit = new Dictionary<string, int> {
        {"one", 1}, 
        {"two", 2}, 
        {"three", 3}, 
        {"four", 4}, 
        {"five", 5}, 
        {"six", 6}, 
        {"seven", 7}, 
        {"eight", 8}, 
        {"nine", 9}, 
        {"zero", 0} 
      };
      
      string pattern = @"(?=(\d|one|two|three|four|five|six|seven|eight|nine))";
      var matches = Regex.Matches(line, pattern);
      
      if (matches.Count == 1) {
        string value = matches[0].Groups[1].Value;
        if (wordToDigit.ContainsKey(value)) {
          wordToDigit.TryGetValue(value, out int1);
          wordToDigit.TryGetValue(value, out int2);
        }
        else {
          int1 = Convert.ToInt32(value);
          int2 = Convert.ToInt32(value);
        }
      }
      else if (matches.Count > 1) {
        string firstValue = matches[0].Groups[1].Value;
        string lastValue = matches[matches.Count - 1].Groups[1].Value;
        
        if (wordToDigit.ContainsKey(firstValue)) {
          wordToDigit.TryGetValue(firstValue, out int1);
        }
        else {
          int1 = Convert.ToInt32(firstValue);
        }
        
        if (wordToDigit.ContainsKey(lastValue)) {
          wordToDigit.TryGetValue(lastValue, out int2);
        }
        else {
          int2 = Convert.ToInt32(lastValue);
        }
      }
      
      return Convert.ToInt32(Convert.ToString(int1) + Convert.ToString(int2));
    }
  }
}
