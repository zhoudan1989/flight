import matplotlib.pyplot as plt

class sample:
    def __init__(self):
        pass

    def getplot(x):
        y = [val ** 2 for val in x]
        z = [val ** 2 + val * 2 for val in x]
        plt.plot(x, y, label="A")
        plt.plot(x, z, label="B")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('1')
        plt.legend()
        return plt.gcf().savefig()