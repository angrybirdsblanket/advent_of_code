namespace Advent_Of_code {
  class Program {
    static async Task Main() {
      await day2b.run();
    }

    public static async IAsyncEnumerable<string> readFile(string filePath) {
      StreamReader sr = new StreamReader(filePath);
      string? line;
      while ((line = await sr.ReadLineAsync()) != null){
        yield return line;
      }
    }
  }
}
