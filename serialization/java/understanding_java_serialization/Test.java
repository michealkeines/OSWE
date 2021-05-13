import java.io.*;

public class Test
{
	public static void main(String[] args)
	{
		LogFile log = new LogFile();
		log.filename = "test.log";
		log.filecontent = "we did something";

		String file = "log.bin";

		Helper.SerializeToFile(log, file);

		// Attack
		
		LogFile vul = new LogFile();
		String filename = "log.bin";

		vul = (LogFile) Helper.DeserializeFromFile(filename);
	}
}
