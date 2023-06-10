import org.aspectj.lang.reflect.*;

public privileged aspect MyAspect {

	declare soft: Throwable: within(MyAspect);

	private pointcut onGet():
		!within(MyAspect) &&
		get(* *) &&
		!execution(public static void Main.main(String[])) &&
		!get(* java..*); 

	Object around(): onGet() {
		System.out.println("===== MyAspect::around =====");
		
		Object field = ((FieldSignature)thisJoinPoint.getSignature())
             										 .getField()
			     									 .get(thisJoinPoint.getTarget());
		if (field == null) 
			throw new RuntimeException();

		return field;
	}

}
