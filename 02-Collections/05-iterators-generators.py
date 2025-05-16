class RemoteControl:
    def __init__(self):
        self.channels = ['POGO', 'HBO', 'LIVE']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = RemoteControl()
for channel in r:
    print("Channel:", channel)


# Simple generator example
def remote_control_next():
    yield 'cnn'
    yield 'pg'

itr = remote_control_next()
print(next(itr))
print(next(itr))
# print(next(itr))  # Will raise StopIteration

# Fibonacci generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for f in fib():
    if f > 50:
        break
    print(f)
