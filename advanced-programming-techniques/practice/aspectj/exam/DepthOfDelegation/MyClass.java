class A {

    void a() {
        System.out.println("A::a");
        new B().b(); // 2
        new B().b2(); // 3
    }

}

class B {

    void b() {
        System.out.println("B::b");
        new C().c();
    }

    void b2() {
        System.out.println("B::b2");
        new D().d();
    }

}

class C {

    void c() {
        System.out.println("C::c");
    }

}

class D {

    void d() {
        System.out.println("D::d");
        new C().c();
    }

}

class Main {

    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        
        a.a();
        b.b();
    }

}
