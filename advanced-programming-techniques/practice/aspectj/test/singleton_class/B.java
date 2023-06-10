@Singleton
public class B {
	
	public int f;
 
	public B(int a) {
		System.out.println("B::new");
		this.f = a;
	}

	public int getF() {
		return this.f;
	}

	public String toString() {
		return "B::toString " + this.f;
	}

}

