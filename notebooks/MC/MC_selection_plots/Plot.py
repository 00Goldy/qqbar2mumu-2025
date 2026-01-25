import matplotlib.pyplot as plt

def Plot(H1, H2=None, 
         labelH1=None, labelH2=None, 
         labelx=None, labely=None,
         title=None, 
         logx=False, logy=False, 
         ratio=False,
         save=False, savename=None):
    """
    Take histograms and plot the figure desired
    :param: example: This is an example of a parameter || format: boolean

    :param: H1: First Histogram || format: hist.Hist
    :param: H2: Second Histogram || format: hist.Hist
    :param: labelH1: Name of what data H1 contains, with eventual cuts || format: string
    :param: labelH2: Name of what data H2 contains, with eventual cuts || format: string
    :param: labelx: Name of the x axis || format: string
    :param: labely: Name of the y axis || format: string
    :param: title: Title of the plot || format: string
    :param: logx: Define if the x axis should be log-ed || format: boolean
    :param: logy: Define if the y axis should be log-ed || format: boolean
    :param: ration: Define if the 2 histograms should be ratioed (H1/H2) || format: boolean
    :param: save: Define if the plot should be saved || format: boolean
    :param: savename: Name of the saved plot || format: string

    """
    plt.figure(figsize=(10, 6))
    
    if ratio:
        result = H1 / H2
        result.plot(label=labelH1 if labelH1 else "Ratio")
        default_ylabel = "Ratio"
    else:
        H1.plot(label=labelH1)
        if H2:
            H2.plot(label=labelH2)
        default_ylabel = "# of tracks"
    
    if logx:
        plt.xscale("log")
    if logy:
        plt.yscale("log")
    
    plt.xlabel(labelx)
    plt.ylabel(labely if labely else default_ylabel)
    plt.title(title if title else "Ratio" if ratio else "Histogram Plot")
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.legend()

    if save:
        if savename:
            plt.savefig(savename+'.png')
        else:
            plt.savefig('YourAwesomePlot.png')

    plt.show()





