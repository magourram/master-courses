import java.util.*;

public privileged aspect MyAspect { 

	/*public static boolean A.isSingleton = false;*/
	/*private Object x;*/
  private HashMap<String, Object> hm = new HashMap<>(); 
	
	private pointcut singleton():
		call((@Singleton *).new(..)) &&
		!cflow(within(MyAspect));

  Object around(): singleton() {
		String sign = thisJoinPoint.getSignature().toString();
		Object o = proceed();
		hm.putIfAbsent(sign, o);
		return hm.get(sign);
	}

	/*Object around(): singleton() {*/
		/*System.out.println("MyAspect::around");*/
		/*Object[] tmp = thisJoinPoint.getArgs();*/
		/*int arg = (int)tmp[0];*/
		/*if (!A.isSingleton) {*/
			/*A.isSingleton = true;*/
			/*x = proceed();	*/
			/*System.out.println("X after proceed: " + x);*/
			/*return x;*/
		/*}*/
		/*return x;*/
	/*}*/
}
