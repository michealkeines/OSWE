import java.io.*;

public class Serial
{
	public static void main(String[] args)
	{
		String name = "Nytro";
		String filename = "file.bin";

		try
		{
			FileOutputStream file = new FileOutputStream(filename);
			ObjectOutputStream out = new ObjectOutputStream(file);

			out.writeObject(name);
			out.close();
			file.close();
		}
		catch (Exception e)
		{
			System.out.println("Fucked: " + e.toString());
		}
	}
}
