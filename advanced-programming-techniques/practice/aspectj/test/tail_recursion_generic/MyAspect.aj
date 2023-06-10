import org.aspectj.lang.SoftException;
import org.aspectj.lang.reflect.*;
import java.util.*;
import java.lang.reflect.*;

public privileged aspect MyAspect percflow(call(* *.*(..)) 
                                        && withincode(* *.main(..))) {

  Object[] args = null;
 
  declare soft: Throwable: within(*);
  /*declare soft: TailException: within(*);*/

  public pointcut trackTail(): 
    call(@TailAnnotation * *.*(..));

  Object around(): trackTail() {
    args = thisJoinPoint.getArgs();
    System.out.println((new Throwable()).getStackTrace().length + " " + MyAspect.aspectOf());
    
    if ((new Throwable()).getStackTrace().length > 3) // if the last stack element is equals to me
        throw new TailException(args);
    else while(true) try {
          return ((MethodSignature)thisJoinPoint.getSignature()).getMethod().invoke(thisJoinPoint.getTarget(), args); 
        } catch(SoftException te) {
          args = ((TailException)((SoftException)((SoftException)te).getWrappedThrowable().getCause()).getWrappedThrowable()).args;
        }
  }

}
