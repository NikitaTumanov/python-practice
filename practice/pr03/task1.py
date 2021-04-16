class C32:
    def __init__(self):
        self.state: C32.State = C32.A(self)

    def drive(self) -> int:
        return self.state.drive()

    def cull(self) -> int:
        return self.state.cull()

    def check(self) -> int:
        return self.state.check()

    def clear(self) -> int:
        return self.state.clear()

    class State:
        def __init__(self, parent):
            self.parent: C32 = parent

        def drive(self) -> int:
            raise RuntimeError

        def cull(self) -> int:
            raise RuntimeError

        def check(self) -> int:
            raise RuntimeError

        def clear(self) -> int:
            raise RuntimeError

    class A(State):
        def drive(self):
            self.parent.state = C32.B(self.parent)
            return 0

    class B(State):
        def cull(self):
            self.parent.state = C32.C(self.parent)
            return 1

    class C(State):
        def check(self):
            self.parent.state = C32.D(self.parent)
            return 2

        def cull(self):
            self.parent.state = C32.E(self.parent)
            return 3

    class D(State):
        def check(self):
            self.parent.state = C32.E(self.parent)
            return 4

    class E(State):
        def drive(self):
            self.parent.state = C32.F(self.parent)
            return 5

    class F(State):
        def check(self):
            self.parent.state = C32.A(self.parent)
            return 9

        def clear(self):
            self.parent.state = C32.F(self.parent)
            return 8

        def cull(self):
            self.parent.state = C32.G(self.parent)
            return 6

        def drive(self):
            self.parent.state = C32.H(self.parent)
            return 7

    class G(State):
        def clear(self):
            self.parent.state = C32.H(self.parent)
            return 10

    class H(State):
        def drive(self):
            self.parent.state = C32.E(self.parent)
            return 11
