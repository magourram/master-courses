public privileged aspect HandleThree extends AbstractAspect {

	after(Test t): handleThree(t) {
		System.out.println("Handle Three");
	}

} 
