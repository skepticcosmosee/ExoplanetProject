import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")

def plot_histogram(data,column,bins=10,title="The Histogram Graph"):
    plt.figure(pltfigsize=(10,6))
    sns.histplot(data[column].dropna(), bins=bins, kde=True)
    plt.title(title if title else f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout() 
    plt.show()
    print("kuc bh krr")
    if __name__ == "__main__":
        from data_loader import load_exoplanet_data
        df = load_exoplanet_data("data/kepler_data.csv")
        plot_histogram(df,'pl_rade')
     

     