import java.lang.Math.*;

public privileged aspect MyAspect percflow(cflowMain()) { 
    
    int base = 0;
    int m = 0;

    pointcut cflowMain():
        call(* *.*(..)) &&
        withincode(public static void *.main(String[])) &&
        !call(* java..*(..)) &&
        !within(MyAspect);

    before(): execution(* *.*(..)) {
        System.out.println(MyAspect.aspectOf());
        int tmp = new Throwable().getStackTrace().length;
        if (m == 0) {
            base = tmp;
        }
        m = Math.max(tmp, m);
    } 

    after(): cflowMain() {
       System.out.println(thisJoinPoint + " " + MyAspect.aspectOf() + " " + (m-base));
    }

}
