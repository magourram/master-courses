public privileged aspect HandleThree extends AbstractAspect {

	pointcut onCall():
		call(* Test.print(..)) &&
		if(h == 3);

	after(Test t): handle(t) {
		if(((Test)t).array.length == 3) {
			h = 3;
		}
	}

	before(): onCall() {
		System.out.println("[THREE]");
	}

} 
