import logging


def log_debug(func):
    def wrap(*args, **kwargs):
        func_name  =func.__qualname__ if not isinstance(func, classmethod) else func.__func__.__qualname__
        extra = {
            'function_name': func_name,
            'func_args': args, 'func_kwargs': kwargs}
        try:
            output = func(*args, **kwargs)
            extra.update({'output': output})
            msg = 'executed without exceptions'
        except Exception as e:
            msg = 'executed with an exception {exception}'.format(exception=e.with_traceback(e.__traceback__))
            extra.update({'output': None})

        logger = get_debug_logger(func_name.split('.')[0], extra=extra)
        if 'without' in msg:
            logger.debug(msg, extra=extra)
        else:
            logger.error(msg, extra=extra)
            # format = '%(asctime)s - %(levelname)s - %(function_name)s - %(func_args)s - %(func_kwargs)s - %(output)s ' \
            # '- %(message)s '
            # logging.basicConfig(format=format, level=logging.DEBUG)
            # loggerConsole = logging.getLogger(__name__)
            # loggerConsole.error(msg, extra=extra)

        # This will maintain the function name and documentation of the wrapped function.
        # Very helpful when debugging or checking the docs from the python shell:
        log_debug.__doc__ = wrap.__doc__
        log_debug.__name__ = wrap.__name__

    return wrap


def callable(o):
    return hasattr(o, "__call__")


def log_methods(cls):
    for key, val in cls.__dict__.items():
        if key.startswith("__") and key.endswith("__") or not callable(val):
            continue
        setattr(cls, key, log_debug(val))
    return cls


def get_debug_logger(cls_name, extra):
    app_logger = logging.getLogger(cls_name)
    handler = logging.FileHandler('PR_Skate/logging/logs/class_method.log')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(function_name)s - %(func_args)s - %(func_kwargs)s - %(output)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S')
    handler.setFormatter(formatter)
    app_logger.addHandler(handler)
    app_logger.setLevel(logging.DEBUG)
    app_logger = logging.LoggerAdapter(app_logger, extra)
    return app_logger
