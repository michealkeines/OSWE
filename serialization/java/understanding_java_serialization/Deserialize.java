import java.io.*;

public class Deserialize
{
	public static void main(String[] args)
	{
		String name;
		String filename = "file.bin";

		try
		{
			FileInputStream file = new FileInputStream(filename);
			ObjectInputStream out = new ObjectInputStream(file);

			name = (String) out.readObject();

			System.out.println(name);
		}
		catch (Exception e)
		{
			System.out.println("Fucked: " + e.toString());
		}
	}
}
