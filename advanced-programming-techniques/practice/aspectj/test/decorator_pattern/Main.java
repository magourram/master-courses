interface Decorateable {
  void doSomething();
}
 
interface Decorator extends Decorateable {
}

class Decorated implements Decorateable {
  public Decorated() {}

  public void doSomething() {
    System.out.println("Decorated::doSomething");
  }
}

class ConcreteDecorator implements Decorator {
  Decorateable decorateable;
  
  public ConcreteDecorator(Decorateable decorateable) { 
    this.decorateable = decorateable; 
  }

  private void concreteSomething() {
    System.out.println("ConcreteDecorator::concreteSomething");
  }

  public void doSomething() {
    decorateable.doSomething();
    concreteSomething();
  }
}

interface I {}

class X implements I, Decorateable {
  public void doSomething() {
    System.out.println("X::doSomething");
  }
}

class Main {

  public static void main(String[] args) {
    Decorated d = new Decorated();
    ConcreteDecorator cd = new ConcreteDecorator(d);
    cd.doSomething();
    
    System.out.println("");

    X x = new X();
    ConcreteDecorator cd2 = new ConcreteDecorator(x);
    cd2.doSomething();
  }

}
