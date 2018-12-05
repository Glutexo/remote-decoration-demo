from replacer import replace
import my_mod

if __name__ == "__main__":
    from getter import get_do_something
    func = get_do_something()
    replace(func)

    print(my_mod.do_something())
