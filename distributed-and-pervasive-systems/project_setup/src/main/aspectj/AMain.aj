public aspect AMain {
    pointcut mainMethod(): 
        execution(public static void main(String[]))
        && !within(AMain);
    
    after(): mainMethod() {
        System.out.println("After main");
    }
}
