public privileged aspect MyAspect4 {

	public pointcut handle():
		execution(Test.new(..)) &&
        !within(MyAspect4);
    
    after(): handle() {
        if(((Test)thisJoinPoint.getTarget()).array.length == 4)
            System.out.println("4");
    }

}
