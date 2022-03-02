import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    patients = False
    if not patients:
        path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/radiomics_features.csv"
        save_path = "hist/"
    else:
        path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/patients_features.csv"
        save_path = "patient_hist/"

    df = pd.read_csv(path, )
    # skewness + kurtosis intervall sehr eng.
    sns.set(style="ticks")
    cmap = sns.color_palette('tab10', n_colors=3)

    if not patients:
        df = df.drop(["Mask", "Image", "Unnamed: 0", "diagnostics_Configuration_EnabledImageTypes", "diagnostics_Configuration_Settings", "diagnostics_Image-Dimensionality",
                      "diagnostics_Image-Maximum", "diagnostics_Image-Mean", "diagnostics_Image-Minimum", "diagnostics_Image-Size", "diagnostics_Image-Spacing",
                      "diagnostics_Mask-BoundingBox", "diagnostics_Mask-CenterOfMass", "diagnostics_Image-Hash",
                      "diagnostics_Mask-CenterOfMassIndex", "diagnostics_Mask-Hash", "diagnostics_Mask-Size", "diagnostics_Mask-Spacing", "diagnostics_Mask-VolumeNum",
                      "diagnostics_Mask-VoxelNum",
                      "diagnostics_Versions_Numpy", "diagnostics_Versions_PyRadiomics", "diagnostics_Versions_PyWavelet", "diagnostics_Versions_Python",
                      "diagnostics_Versions_SimpleITK"], axis=1)

    if patients:
        df = df.drop(["Image", "Unnamed: 0"], axis=1)
    # iterate over the columns.
    col = df.columns

    for c in col:
        sns_plot = sns.displot(df, x=c, hue="Gruppe", kind="kde", palette=cmap)
        # sns_plot = sns.displot(df, x=c, bins=20, hue="Gruppe")
        plt.close()
        sns_plot.savefig(save_path + c + ".png")


if __name__ == '__main__':
    main()
