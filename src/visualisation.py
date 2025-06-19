import matplotlib.pyplot as plt
import seaborn as sns

<<<<<<< HEAD
sns.set(style="whitegrid")

def plot_histogram(data, column, bins=10, title="The Histogram Graph"):
    plt.figure(figsize=(10, 6))  # fixed here
=======

sns.set(style="whitegrid")

def plot_histogram(data,column,bins=10,title="The Histogram Graph"):
    plt.figure(pltfigsize=(10,6))
>>>>>>> a55c392c9cdcab26ea22f60a8b5b3eda68e73dab
    sns.histplot(data[column].dropna(), bins=bins, kde=True)
    plt.title(title if title else f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
<<<<<<< HEAD
    plt.tight_layout()
    plt.show()
    print("dekh kar rha hai?")

if __name__ == "__main__":
    from data_loader import load_exoplanet_data
    df = load_exoplanet_data("data/kepler_data.csv")
    plot_histogram(df, 'pl_rade')
=======
    plt.tight_layout() 
    plt.show()
    print("kuc bh krr")
    if __name__ == "__main__":
        from data_loader import load_exoplanet_data
        df = load_exoplanet_data("data/kepler_data.csv")
        plot_histogram(df,'pl_rade')
     

     
>>>>>>> a55c392c9cdcab26ea22f60a8b5b3eda68e73dab
