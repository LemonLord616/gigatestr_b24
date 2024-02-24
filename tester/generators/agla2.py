import random

from .abs_generator import AbsGenerator


def gen_matrix(m, n, float_=False, range_=(-5, 5)) -> str:
    r = ""
    for i in range(m):
        for j in range(n):
            if float_:
                r += f"{round(random.random() * (range_[1] - range_[0]) - range_[0], 2)} "
            else:
                r += f"{random.randint(range_[0], range_[1])} "
        r += '\n'
    return r


class GeneratorAgla2Task1(AbsGenerator):
    @staticmethod
    def generate() -> str:
        if random.randint(0, 1):
            m2 = m1 = random.randint(1, 4)
            n2 = n1 = random.randint(1, 4)
        else:
            m1 = random.randint(1, 4)
            n1 = random.randint(1, 4)
            m2 = random.randint(1, 4)
            n2 = random.randint(1, 4)
        m3 = random.randint(1, 4)
        n3 = random.randint(1, 4)

        return f"{m1}\n{n1}\n{gen_matrix(m1, n1)}{m2}\n{n2}\n{gen_matrix(m2, n2)}{m3}\n{n3}\n{gen_matrix(m3, n3)}"


class GeneratorAgla2Task2(AbsGenerator):
    @staticmethod
    def generate() -> str:
        if random.randint(0, 1):
            n2 = n1 = random.randint(1, 4)
        else:
            n1 = random.randint(1, 4)
            n2 = random.randint(1, 4)
        n3 = random.randint(1, 4)

        return f"{n1}\n{gen_matrix(n1, n1)}{n2}\n{gen_matrix(n2, n2)}{n3}\n{gen_matrix(n3, n3)}"


class GeneratorAgla2Task3(AbsGenerator):
    @staticmethod
    def generate() -> str:
        n = random.randint(1, 4)
        return f"{n}\n{gen_matrix(n, n)}"


class GeneratorAgla2Task4(AbsGenerator):
    @staticmethod
    def generate() -> str:
        n = random.randint(1, 4)
        return f"{n}\n{gen_matrix(n, n, bool(random.randint(0, 1)))}"


class GeneratorAgla2Task5(AbsGenerator):
    @staticmethod
    def generate() -> str:
        return GeneratorAgla2Task4.generate()


class GeneratorAgla2Task6(AbsGenerator):
    @staticmethod
    def generate() -> str:
        n = random.randint(1, 4)
        return f"{n}\n{gen_matrix(n, n)}{n}\n{gen_matrix(1, n)}"


__all__ = [
    'GeneratorAgla2Task1',
    'GeneratorAgla2Task2',
    'GeneratorAgla2Task3',
    'GeneratorAgla2Task4',
    'GeneratorAgla2Task5',
    'GeneratorAgla2Task6',
]