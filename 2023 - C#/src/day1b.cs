namespace Advent_Of_code {
  class day1b {

    public static async Task run() {

      await foreach (string line in Program.readFile("../data/2023/day1test.txt")) {
        Console.WriteLine(line);
      }

    }

  }

}
