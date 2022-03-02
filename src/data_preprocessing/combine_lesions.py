import numpy as np
import pandas as pd


def main():

    path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/radiomics_features.csv"

    df = pd.read_csv(path)
    df = df.drop(["Mask", "Unnamed: 0", "diagnostics_Configuration_EnabledImageTypes", "diagnostics_Configuration_Settings", "diagnostics_Image-Dimensionality",
                  "diagnostics_Image-Maximum", "diagnostics_Image-Mean", "diagnostics_Image-Minimum", "diagnostics_Image-Size", "diagnostics_Image-Spacing",
                  "diagnostics_Mask-BoundingBox", "diagnostics_Mask-CenterOfMass", "diagnostics_Image-Hash",
                  "diagnostics_Mask-CenterOfMassIndex", "diagnostics_Mask-Hash", "diagnostics_Mask-Size", "diagnostics_Mask-Spacing", "diagnostics_Mask-VolumeNum",
                  "diagnostics_Mask-VoxelNum",
                  "diagnostics_Versions_Numpy", "diagnostics_Versions_PyRadiomics", "diagnostics_Versions_PyWavelet", "diagnostics_Versions_Python",
                  "diagnostics_Versions_SimpleITK"], axis=1)
    # iterate over the columns.
    col = df.columns
    # get all the names
    names = df.Image

    # define unique names.
    names = np.unique(names)
    patient_list = pd.DataFrame([], columns=col)
    # select all the names then create new dataframe and add the row.
    for n in names:
        # select all the rows with the patient name
        sub = df[df.Image == n]

        # mean all of the columns.
        mean_list = pd.Series()
        i = 0
        for x in df.columns:
            if x == "Image" or x == "Gruppe":
                continue
            mean_list.at[i] = sub[x].mean()
            i += 1

        patient = sub.iloc[0, :2]

        patient = patient.append(mean_list)
        # build new dataframe.
        patient_list = patient_list.append(patient, ignore_index=True)

    patient_list.to_csv("/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/patients_features.csv")
    #df.to_csv("/home/mfmezger/data/AI_Clinic_Data/LissonCat/Excel/features_all.csv")

if __name__ == '__main__':
    main()