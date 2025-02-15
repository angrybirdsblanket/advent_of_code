using System.Text.RegularExpressions;

namespace Advent_Of_code {
  class day2a {
    public static async Task run() {

      Dictionary<int, string[]> games = new Dictionary<int, string[]> {};

      int game_id_sum = 0;
      await foreach (string line in Program.readFile("../data/2023/day2.txt")) {
        game_id_sum += validate_game(Convert.ToInt32(line.Split(':')[0].Replace("Game ", "")) , line.Split(":")[1].Split(';'));
      }
      Console.WriteLine(game_id_sum);

    }

    static int validate_game(int id, string[] games) {
      string pattern = @"(\d+ red|\d+ blue|\d+ green)";

      foreach(string game in games) {
        int red = 12; int green = 13; int blue = 14;
        var matches = Regex.Matches(game, pattern);
        foreach (Match match in matches) {
          switch (match.Value.Split(" ")[1]) {
            case "red":
              red -= Convert.ToInt32(match.Value.Split(" ")[0]);
              break;
            case "blue":
              blue -= Convert.ToInt32(match.Value.Split(" ")[0]);
              break;
            case "green":
              green -= Convert.ToInt32(match.Value.Split(" ")[0]);
              break;
          }
          if (red < 0 || green < 0 || blue < 0) {
            return 0;
          }
        }
      }

      return id;
    }
  }
}
