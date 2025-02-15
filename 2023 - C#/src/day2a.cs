using System.Text.RegularExpressions;

namespace Advent_Of_code {
  class day2a {
    public static async Task run() {

      Dictionary<int, string[]> games = new Dictionary<int, string[]> {};

      int game_id_sum = 0;
      await foreach (string line in Program.readFile("../data/2023/day2test.txt")) {
        game_id_sum += validate_game(Convert.ToInt32(line.Split(":")[0]) - '0', line.Split(":")[1].Split(';'));
      }

    }

    static int validate_game(int id, string[] games) {
      string pattern = @"(\d+ red|\d+ blue|\d+ green)";
      int red = 12; int green = 13; int blue = 14;
      string[] colours = {"red", "blue", "green"};
 
      foreach(string game in games) {
        var matches = Regex.Matches(game, pattern);
      }

      return id;
    }
  }
}
