import matplotlib.pyplot as plt
import clipboardplot


def figure():
    print(dir(plt.figure))
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()