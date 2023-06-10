privileged public aspect WhereAreAll {
  pointcut calls(): call(* *.*(..)) ;
  pointcut execs(): execution(* *.*(..)) ;
  pointcut cnews(): call(*.new(..)) ;
  pointcut enews(): execution(*.new(..)) ;
  pointcut sets():  set(* *.*);
  pointcut gets():  get(* *.*);
  pointcut inits(): initialization(*.new(..));
  pointcut pinits(): preinitialization(*.new(..));
  pointcut sinits(): staticinitialization(*);
  pointcut catches(): handler(*);
  pointcut all(): (calls() || execs() ||
                   cnews() || enews() ||
                   gets()  || sets()  ||
                   inits() || pinits() || sinits()) && !within(WhereAreAll) ;

  before(): all() || catches() {
    System.out.println("[B]["+thisJoinPoint.getSourceLocation()+"] "+thisJoinPoint);
  }

  after(): all() { 
    System.out.println("[A]["+thisJoinPoint.getSourceLocation()+"] "+thisJoinPoint);
  }
}
