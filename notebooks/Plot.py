import matplotlib.pyplot as plt
def Plot(H1, H2=None, labelH1=None, labelH2=None, xlabel=None, ylabel=None, title=None, logx=False, logy=False, ratio=False):
    plt.figure(figsize=(10, 6))
    
    if ratio:
        result = H1 / H2
        result.plot(label="Ratio")
        default_ylabel = "Ratio"
    else:
        H1.plot(label=labelH1)
        if H2 is not None:
            H2.plot(label=labelH2)
        default_ylabel = "# of tracks"
    
    if logx:
        plt.xscale("log")
    if logy:
        plt.yscale("log")
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel if ylabel else default_ylabel)
    plt.title(title if title else "Histogram Plot")
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()