import datetime as d


def logger(file_path):
    def logger_(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(file_path, 'a', encoding="utf-8") as f:
                f.write(f'{d.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                f.write(f'Вызвана функция {old_function.__name__}\n')
                f.write(f'с аргументами {args} и {kwargs}\n')
                f.write(f'результат {result}\n')
                f.write('-'*120)
                f.write('\n')
            return result
        return new_function
    return logger_