class Dummy {}

public class Test {

	private Dummy dummy;
	private Dummy dummy2;

	public Test(Dummy dummy) {
		if (dummy == null) {
			this.dummy = new Dummy();
		}
		this.dummy = dummy;
	}

	public Dummy getDummy() {
		System.out.println("Dummy::getDummy");
		return this.dummy;
	}

	public Dummy getDummy2() {
		System.out.println("Dummy::getDummy2");
		return this.dummy2;
	}

}

