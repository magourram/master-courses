public privileged aspect MyAspect3 {

	public pointcut handle():
		execution(Test.new(..)) &&
        !within(MyAspect3);

    after(): handle() {
        if(((Test)thisJoinPoint.getTarget()).array.length == 3)
            System.out.println("3");
    }

}
