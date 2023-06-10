public class Test {

	private Object n = 0;
	private Object[] array;

	public Test(Object n, Object[] array) {
		this.array = array;
		this.n = n;
	}

	public void print() {
		for (Object o : this.array) {
			System.out.print(o);
		}
		System.out.println();
	}
} 
