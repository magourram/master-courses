public abstract privileged aspect AbstractAspect {

	static int h = -1;

	public pointcut handle(Test t):
		execution(Test.new(..)) &&
		target(t);

	abstract pointcut onCall();

}
