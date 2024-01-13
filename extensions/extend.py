def extend(class_):
    def wrapper(func):
        def inner(*args, **kwargs):
            args_list = ", ".join(str(a) for a in args)
            kwargs_list = ", ".join([f"{k}={w}" for k, w in kwargs.items()])
            whole_list = ", ".join(l for l in [args_list, kwargs_list] if l != "")
            print(f"{func.__name__}({whole_list})")
            func(*args, **kwargs)

        return inner

    return wrapper
