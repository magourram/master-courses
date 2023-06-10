public class B {
	
	public void b() {
		System.out.println("B::b");
		//new D().d();
		new C().c();
	}

	public void b2() {
		System.out.println("B::b2");
		new D().d();
		
	}
}
