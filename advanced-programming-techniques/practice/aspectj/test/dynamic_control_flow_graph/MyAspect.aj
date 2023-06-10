import org.aspectj.lang.reflect.*;
import java.lang.reflect.*;
import java.lang.annotation.*;

public privileged aspect MyAspect pertarget(onCall()) {

    private pointcut onCall():
        call(@AnnotationGraph * *.*(..));
     
    after(): onCall() {
        Method m = ((MethodSignature)thisJoinPoint.getSignature()).getMethod();
        AnnotationGraph ag = (AnnotationGraph)m.getAnnotation(AnnotationGraph.class);
        for (Class<?> to : ag.value())
            Graph.addEdge(m.getDeclaringClass().toString(), m.getName().toString(), to.toString());
    }     
    
}
