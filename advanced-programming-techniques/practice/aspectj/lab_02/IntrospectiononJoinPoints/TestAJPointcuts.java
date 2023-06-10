public class TestAJPointcuts {
  private static int data;
  public String name;

  public TestAJPointcuts() {
     this.name = "dummy" ;
  }

  static public int init() { return 42; }

  public void accessToNull() {
    try {
      TestAJPointcuts t = null;
      System.out.println(t.toString());
    } catch(NullPointerException e) {
      e.printStackTrace();
    }
  }

  public String toString() {
    return "name :- "+this.name+"\ndata :- "+TestAJPointcuts.data;
  }

  static {
    data = init();
  }

  public static void main(String[] args) {
     TestAJPointcuts taj = new TestAJPointcuts();

     System.out.println(taj);

     taj.accessToNull();
  }
}
