import java.util.*;
import org.aspectj.lang.JoinPoint;

public privileged aspect MyAspect2 {

	ArrayList<ArrayList<String>> myList = new ArrayList<ArrayList<String>>();	
	
	{
		myList.add(new ArrayList());
	}
	
	int pos = 0;
	int depth = -1;

	private pointcut track():
		cflowbelow(execution(public static void Main.main(String[]))) &&
		execution(* *.*(..)) &&
		!within(MyAspect2);

	before(): track() {
		int steLength = (new Throwable()).getStackTrace().length;
		if (steLength < depth) {
			myList.add(new ArrayList());
			pos++;
		}
		myList.get(pos).add(createString(thisJoinPoint));	
		depth = steLength;
	} 
	
	after(): execution(public static void Main.main(String[])) {
		int max = 0;
		for (ArrayList al : myList) {
			max = myList.get(max).size() < al.size() ? myList.indexOf(al) : max; 
		}
		System.out.println(myList.get(max));
	}

	private String createString(JoinPoint jp) {
		return jp.getSignature().toString() + " " + Arrays.asList(jp.getArgs()).toString();
	} 

}

