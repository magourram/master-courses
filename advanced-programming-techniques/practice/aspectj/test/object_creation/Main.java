public class Main {
	
	String s;

	public Main(String s) {
		this.s = s;
	}

	public int mInt() {
		return 1;
	}

	public String mString() {
		return "s";
	}

	public static void main(String[] args) {
		Main main = new Main("main");
		main.mInt();
		main.mString();
	}

}
