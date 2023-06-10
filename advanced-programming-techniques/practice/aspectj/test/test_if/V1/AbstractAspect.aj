public abstract privileged aspect AbstractAspect {

	public pointcut handleThree(Test t):
		execution(Test.new(..)) &&
		target(t) &&
		if(((Test)t).array.length == 3);

	public pointcut handleFour(Test t):
		execution(Test.new(..)) &&
		target(t) &&
		if(((Test)t).array.length == 4);

}
