def guarded(F_guarder):
    def decorator(F):
        def wrapper(*args):
            if F_guarder(*args[1:]):
                return F(*args)
        return wrapper
    return decorator
