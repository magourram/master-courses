public privileged aspect HandleFour extends AbstractAspect {

	after(Test t): handleFour(t) {
		System.out.println("Handle Four");
	}

} 
 
