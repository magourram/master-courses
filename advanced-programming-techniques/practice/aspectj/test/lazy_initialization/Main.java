public class Main {

	public static void main(String[] args) {
		Test test = new Test(new Dummy());
		System.out.println(test.getDummy());
		System.out.println();
		System.out.println(test.getDummy2());
	}

}
