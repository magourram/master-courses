import java.io.*;
import org.aspectj.lang.SoftException;

public privileged aspect AExceptionHandler {

    // ===== I could have used Exception =====
    declare soft: 
        FileNotFoundException: 
            call(* *.*(..) throws *) && 
            !within(AExceptionHandler);

    declare soft: 
        IOException: 
            call(* *.*(..) throws *) && 
            !within(AExceptionHandler);
    

    declare soft: 
        FileNotFoundException: 
            call(*.new(..) throws *) && 
            !within(AExceptionHandler);

    declare soft: 
        IOException: 
            call(*.new(..) throws *) && 
            !within(AExceptionHandler);
    // ======================================

    after() throwing(SoftException e): 
        (execution(* *.*(..)) || execution(*.new(..))) &&
         !within(AExceptionHandler) {
        Throwable t = e.getWrappedThrowable();
        StackTraceElement[] ste = t.getStackTrace();
        System.out.println(ste[0].getLineNumber() + 
                     " " + ste[0].getClassName() + 
                     " " + ste[0].getMethodName() + 
                     " " + ste[0].getFileName() +
                     " " + t.getClass());
        System.exit(0);
    }



}
