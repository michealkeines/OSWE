import java.io.*;
import java.lang.reflect.Constructor;

public class ManualPayloadGenerateBlog
{
	public static void main(String[] args) throws IOException, ClassNotFoundException, InstantiationException, IllegalAccessException 
	{
		String classToSerialize = "sun.reflect.annotation.AnnotationInvocationHandler";

		final Constructor<?> constructor = Class.forName(classToSerialize).getDeclaredConstructors()[0];
		constructor.setAccessible(true);

	}
}
