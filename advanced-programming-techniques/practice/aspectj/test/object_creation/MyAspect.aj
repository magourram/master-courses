public privileged aspect MyAspect { 

	pointcut calls(): call(* *.*(..)) ;
  pointcut execs(): execution(* *.*(..)) ;
  pointcut cnews(): call(*.new(..)) ;
  pointcut enews(): execution(*.new(..)) ;
	pointcut sets():  set(* *.*);
	pointcut gets():  get(* *.*);
	pointcut inits(): initialization(*.new(..));
	pointcut pinits(): preinitialization(*.new(..));
	pointcut sinits(): staticinitialization(*);
	pointcut catches(): handler(*);
  pointcut all(): (calls() || execs() || 
                   cnews() || enews() ||
                   gets()  || sets()  ||
                   inits() || pinits() || sinits()) && !within(MyAspect);

	Object around(): all() {
		System.out.println(thisJoinPoint.toLongString());
		Object o = proceed();
		System.out.println("\tObject: " + o);
		System.out.println("----- end -----");
		return o;
	}

}

