
# 3 метода из NumPy


class FirstMethod:
    def gen_zero(self, count):
        return [float(0) for i in range(count)]

    def repeat_list_zero(self, count, *args, ):
        current_list = list(args[0])
        return [current_list for i in range(count)]

# Реализация метода zeros

    def zeros(self, *args):
        params = args[0]
        if type(params) is not tuple:
            return self.gen_zero(params)

        if len(params) == 2:
            return self.repeat_list_zero(params[0], self.gen_zero(params[1]))

        result = self.repeat_list_zero(params[0], self.gen_zero(params[1]))

        for i in params[2:]:
            result = self.repeat_list_zero(i, result)
        return result

# Реализация метода arange

    def arrange(self, start=0.0, stop=0.0, step=0.0):
        array = []
        if stop == 0:
            if start is int:
                return [i for i in range(start)]
            else:
                return [float(i)  for i in range(int(start))]

        if stop != 0 and step == 0:
            while start < stop:
                array.append(start)
                start += 1
            return array
        if stop != 0 and step != 0:
            while start < stop:
                array.append(start)
                start += step
            return array

# Реализация метода linspace

    def linspace(self, a,b,c):
        step =  (b-a) / (c-1)
        array = []
        while a <= b:
            array.append(a)
            a+=step
        return array


q = FirstMethod()

print(q.zeros((2, 4, 2)))

print(q.arrange(3.2))
print(q.arrange(2, 3, 0.1))

print(q.linspace(0,3,9))
