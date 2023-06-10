@Singleton
public class A {
	
	public int f;
 
	public A(int a) {
		System.out.println("A::new");
		this.f = a;
	}

	public int getF() {
		return this.f;
	}

	public String toString() {
		return "A::toString " + this.f;
	}

}
