import java.io.*;

public class LogFile implements Serializable 
{
	public String filename;
	public String filecontent;

	private void readObject(ObjectInputStream in)
	{
		System.out.println("readObject from LogFile");

		try
		{
			in.defaultReadObject();
			System.out.println("File name: " + filename + ", file content: \n" + filecontent);

			FileWriter file = new FileWriter(filename);
			BufferedWriter out = new BufferedWriter(file);

			System.out.println("Writing log data to file...");
			out.write(filecontent);

			out.close();
			file.close();
		}
		catch (Exception e)
		{
			System.out.println("Fucked: " + e.toString());
		}
	}
}
