import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    path = "/home/mfmezger/data/AI_Clinic_Data/adeno_outlier_removed.csv"
    save_path = "outlier_removed/"

    df = pd.read_csv(path, )
    # skewness + kurtosis intervall sehr eng.
    sns.set(style="ticks")
    #cmap = sns.color_palette('tab10', n_colors=10)

    df = df.drop(["Unnamed: 0", "Patient", "Voxels", "G", "cT", "cN", "cM", "pT", "pN", "pM"], axis=1)
    # df = df.drop(["Unnamed: 0", "Patient", "Voxels"], axis=1)

    # iterate over the columns.
    col = df.columns

    for c in col:
        if c == "Stadium" or c == "Histologie":
            continue
        sns_plot = sns.displot(df, x=c, hue="Stadium", kind="kde")
        # sns_plot = sns.displot(df, x=c, bins=20, hue="Gruppe")
        plt.close()
        sns_plot.savefig(save_path + c + ".png")


if __name__ == '__main__':
    main()
