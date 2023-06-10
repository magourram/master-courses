import java.util.*;

public privileged aspect MyAspect {

	ArrayList<StackTraceElement> deeper = new ArrayList<StackTraceElement>();
	ArrayList<Object[]> args = new ArrayList<Object[]>();

	private pointcut track():
		execution(* *.*(..)) &&
		!within(MyAspect) &&
		cflow(execution(public static void Main.main(String[])));

	after(): track() {
		StackTraceElement[] ste = (new Throwable()).getStackTrace();
		if (ste.length > deeper.size())
			deeper = new ArrayList(Arrays.asList(ste));
		args.add(thisJoinPoint.getArgs());
	}

	after(): execution(public static void Main.main(String[])) {
		for (int i = 1; i < deeper.size(); i++)
			System.out.println(deeper.get(i).getClassName() + "." + deeper.get(i).getMethodName() + "(" + Arrays.asList(args.get(i-1)).toString().replaceAll("[\\[\\]]","") + ")");

	}
}
