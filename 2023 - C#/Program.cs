namespace Advent_Of_code {
  class Entry {
    static async Task Main() {
      int sum = 0;
      await foreach (string line in readFile("../data/2023/day1test.txt")) {
        Console.WriteLine(line);
      }
    }

    static async IAsyncEnumerable<string> readFile(string filePath) {
      StreamReader sr = new StreamReader(filePath);
      string? line;
      while ((line = await sr.ReadLineAsync()) != null){
        yield return line;
      }
    }
  }
}
