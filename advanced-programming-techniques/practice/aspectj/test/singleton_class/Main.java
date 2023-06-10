public class Main {

	public static void main(String[] args) {
		A a = new A(10);
		A a2 = new A(20);
    
		System.out.println(a.getF());
		System.out.println(a2.getF());
		
		B b = new B(30);
		B b2 = new B(40);
    
		System.out.println(b.getF());
		System.out.println(b2.getF());
	}

}
