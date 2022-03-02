import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    patients = True
    if not patients:
        path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/radiomics_features.csv"
        save_path = "hist/"
    else:
        path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/patients_features.csv"
        save_path = "patient_hist/"

    df = pd.read_csv(path, )
    # skewness + kurtosis intervall sehr eng.
    sns.set(style="ticks")

    results = pd.DataFrame([], columns=["Feature", "Gruppe", "Mean", "Median", "Std", "Skewness", "Kurtosis"])

    if not patients:
        df = df.drop(["Mask", "Unnamed: 0", "diagnostics_Configuration_EnabledImageTypes", "diagnostics_Configuration_Settings", "diagnostics_Image-Dimensionality",
                      "diagnostics_Image-Maximum", "diagnostics_Image-Mean", "diagnostics_Image-Minimum", "diagnostics_Image-Size", "diagnostics_Image-Spacing",
                      "diagnostics_Mask-BoundingBox", "diagnostics_Mask-CenterOfMass", "diagnostics_Image-Hash",
                      "diagnostics_Mask-CenterOfMassIndex", "diagnostics_Mask-Hash", "diagnostics_Mask-Size", "diagnostics_Mask-Spacing", "diagnostics_Mask-VolumeNum",
                      "diagnostics_Mask-VoxelNum",
                      "diagnostics_Versions_Numpy", "diagnostics_Versions_PyRadiomics", "diagnostics_Versions_PyWavelet", "diagnostics_Versions_Python",
                      "diagnostics_Versions_SimpleITK"], axis=1)

    if patients:
        df = df.drop(["Unnamed: 0"], axis=1)
    # iterate over the columns.
    col = df.columns

    for c in col:
        # select sub dataframe for every class
        if c == "Gruppe" or c == "Image":
            continue
        tmp_df = df[["Image", "Gruppe", c]]
        for i in range(1,4):
            tmp = tmp_df[tmp_df.Gruppe == i]

            # calculate statistical features for every class

            gruppe = i
            mean = tmp.mean(axis=0)[1]
            median = tmp.median(axis=0)[1]
            std = tmp.std(axis=0)[1]
            skew = tmp.skew(axis=0)[1]
            kurtosis = tmp.kurtosis(axis=0)[1]

            # create empty dataframe
            feature = pd.DataFrame([[c, gruppe, mean, median, std, skew, kurtosis]], columns=["Feature", "Gruppe", "Mean", "Median", "Std", "Skewness", "Kurtosis"])
            results = results.append(feature.loc[0], ignore_index=True)

    results.to_csv("patient_features.csv")


if __name__ == '__main__':
    main()
