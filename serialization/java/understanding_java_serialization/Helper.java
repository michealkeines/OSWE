import java.io.*;

public class Helper 
{
	public static void SerializeToFile(Object obj, String filename)
	{
		try
		{
			FileOutputStream file = new FileOutputStream(filename);
			ObjectOutputStream out = new ObjectOutputStream(file);

			System.out.println("Serializing " + obj.toString() + " to " + filename);
			out.writeObject(obj);

			out.close();
			file.close();
		}
		catch(Exception e)
		{
			System.out.println("Exception: " + e.toString());
		}
	}

	public static Object DeserializeFromFile(String filename) 
	{
		Object obj = new Object();

		try
		{
			FileInputStream file = new FileInputStream(filename);
			ObjectInputStream in = new ObjectInputStream(file);

			System.out.println("Deserializing from " + filename);
			obj = in.readObject();

			in.close();
			file.close();
		}
		catch(Exception e)
		{
			System.out.println("Exception: " + e.toString());
		}

		return obj;
	}
}
