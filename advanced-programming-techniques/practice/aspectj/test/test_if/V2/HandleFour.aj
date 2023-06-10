public privileged aspect HandleFour extends AbstractAspect {
	
	pointcut onCall():
		call(* Test.print(..)) &&
		if(h == 4);

	after(Test t): handle(t) {
		if(((Test)t).array.length == 4) {
			h = 4;
		}
	}

	before(): onCall() {
		System.out.println("[FOUR]");
	}

} 
 
