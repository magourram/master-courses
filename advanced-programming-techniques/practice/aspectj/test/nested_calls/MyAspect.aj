import org.aspectj.lang.reflect.*;

public privileged aspect MyAspect {

	int nCalls = 0;

	public pointcut calls():
		call(* NestedCalls.*(..));

	Object around(): calls() {
		nCalls += 1;
		System.out.println(count(nCalls) + " " + ((MethodSignature)thisJoinPoint.getSignature()).getMethod().getName());
		Object o = proceed();
		nCalls -= 1;
		return o;
	}

	private String count(int nCalls) {
		String s = "";
		for (int i = 0; i < nCalls; i++) {
			s += "#";
		}
		return s;
	}

}
