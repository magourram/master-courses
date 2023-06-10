public privileged aspect MyAspect {

  private pointcut noOtherInterface():
    call(* *.new(..)) &&
    !within(MyAspect);
  
  before(): noOtherInterface() {
    Obejct[] args = thisJointPoint.getArgs();
  }
}
