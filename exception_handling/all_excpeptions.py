def raise_exceptions():
    # 1. ArithmeticError - Example: division by zero
    try:
        print("ArithmeticError example:")
        result = 1 / 0
    except ArithmeticError as e:
        print(f"Caught: {e}")

    # 2. AssertionError - Example: failed assertion
    try:
        print("AssertionError example:")
        assert False, "Assertion failed!"
    except AssertionError as e:
        print(f"Caught: {e}")

    # 3. AttributeError - Example: accessing undefined attribute
    try:
        print("AttributeError example:")
        obj = None
        obj.some_method()
    except AttributeError as e:
        print(f"Caught: {e}")

    # 4. EOFError - Example: unexpected end of file/input
    try:
        print("EOFError example:")
        input("Simulate EOFError by pressing Ctrl+D or Ctrl+Z")
    except EOFError as e:
        print(f"Caught: {e}")

    # 5. FloatingPointError - Example: floating point operation error (rare in Python)
    try:
        print("FloatingPointError example:")
        import math
        math.error()
    except FloatingPointError as e:
        print(f"Caught: {e}")

    # 6. GeneratorExit - Example: exiting a generator
    try:
        print("GeneratorExit example:")
        def gen():
            try:
                yield
            finally:
                raise GeneratorExit()
        g = gen()
        next(g)
        g.close()
    except GeneratorExit as e:
        print(f"Caught: {e}")

    # 7. ImportError - Example: importing non-existing module
    try:
        print("ImportError example:")
        import nonexistent_module
    except ImportError as e:
        print(f"Caught: {e}")

    # 8. IndexError - Example: index out of range in a list
    try:
        print("IndexError example:")
        lst = [1, 2, 3]
        print(lst[10])
    except IndexError as e:
        print(f"Caught: {e}")

    # 9. KeyError - Example: key not found in a dictionary
    try:
        print("KeyError example:")
        d = {'a': 1}
        print(d['b'])
    except KeyError as e:
        print(f"Caught: {e}")

    # 10. KeyboardInterrupt - Example: simulating Ctrl+C interrupt
    try:
        print("KeyboardInterrupt example:")
        print("Interrupt with Ctrl+C to simulate KeyboardInterrupt")
        while True:
            pass
    except KeyboardInterrupt as e:
        print(f"Caught: {e}")

    # 11. MemoryError - Example: consuming too much memory (simulate lightly)
    try:
        print("MemoryError example:")
        large_list = [0] * (10 ** 10)
    except MemoryError as e:
        print(f"Caught: {e}")

    # 12. NameError - Example: accessing undefined variable
    try:
        print("NameError example:")
        print(undefined_variable)
    except NameError as e:
        print(f"Caught: {e}")

    # 13. NotImplementedError - Example: method not implemented
    try:
        print("NotImplementedError example:")
        class Base:
            def method(self):
                raise NotImplementedError("This method is not implemented")
        obj = Base()
        obj.method()
    except NotImplementedError as e:
        print(f"Caught: {e}")

    # 14. OSError - Example: performing an invalid file operation
    try:
        print("OSError example:")
        open('/path/to/nonexistent/file.txt', 'r')
    except OSError as e:
        print(f"Caught: {e}")

    # 15. OverflowError - Example: exceeding maximum limit for integers (only in explicit float operations)
    try:
        print("OverflowError example:")
        import math
        math.exp(1000)
    except OverflowError as e:
        print(f"Caught: {e}")

    # 16. ReferenceError - Example: weak reference accessed after object deletion
    try:
        print("ReferenceError example:")
        import weakref
        class A: pass
        a = A()
        r = weakref.ref(a)
        del a
        print(r())
    except ReferenceError as e:
        print(f"Caught: {e}")

    # 17. RuntimeError - Example: re-entering a generator
    try:
        print("RuntimeError example:")
        def gen():
            yield
        g = gen()
        next(g)
        next(g)  # This will cause a RuntimeError
    except RuntimeError as e:
        print(f"Caught: {e}")

    # 18. StopIteration - Example: Iterating beyond the end of an iterator
    try:
        print("StopIteration example:")
        it = iter([1])
        next(it)
        next(it)
    except StopIteration as e:
        print(f"Caught: {e}")

    # 19. SyntaxError - Example: invalid syntax (This cannot be caught directly as it’s a compile-time error)
    try:
        print("SyntaxError example:")
        eval('x === y')
    except SyntaxError as e:
        print(f"Caught: {e}")

    # 20. SystemError - Example: generic interpreter issue
    try:
        print("SystemError example:")
        raise SystemError("Simulated SystemError")
    except SystemError as e:
        print(f"Caught: {e}")

    # 21. SystemExit - Example: system exit
    try:
        print("SystemExit example:")
        import sys
        sys.exit(0)
    except SystemExit as e:
        print(f"Caught: {e}")

    # 22. TypeError - Example: operation with incorrect types
    try:
        print("TypeError example:")
        print(5 + '5')
    except TypeError as e:
        print(f"Caught: {e}")

    # 23. UnboundLocalError - Example: referencing local variable before assignment
    try:
        print("UnboundLocalError example:")
        def func():
            print(x)
            x = 1
        func()
    except UnboundLocalError as e:
        print(f"Caught: {e}")

    # 24. UnicodeError - Example: encoding/decoding issues
    try:
        print("UnicodeError example:")
        b'\x80abc'.decode('utf-8')
    except UnicodeError as e:
        print(f"Caught: {e}")

    # 25. ValueError - Example: invalid value passed
    try:
        print("ValueError example:")
        int('abc')
    except ValueError as e:
        print(f"Caught: {e}")

    # 26. ZeroDivisionError - Example: division by zero
    try:
        print("ZeroDivisionError example:")
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"Caught: {e}")

if __name__ == "__main__":
    raise_exceptions()
