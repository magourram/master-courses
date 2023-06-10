public class Main {
    
  @TailAnnotation  
  public int factorial(int n, int tail) {
    //new Main().fibonacci(10,0,1);
    if (n == 1) {
      return tail;
    } else {
      return factorial(n - 1, tail * n);
    }
  }
 
  @TailAnnotation
  public int fibonacci(int n, int a, int b) {
    if (n == 0)
      return a;
    if (n == 1)
      return b;
    return fibonacci(n - 1, b, a + b);
  }

  public int factorial(int a) {
    return factorial(a, 1);
  }

  public static void main(String[] args) {
    Main m = new Main();
    int res = m.factorial(10);
    System.out.println(res);
    res = m.fibonacci(10, 0, 1);
    System.out.println(res);
  }
}
