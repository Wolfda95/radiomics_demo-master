import os
import pandas as pd


def main():

    path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/"

    df = pd.DataFrame([], columns=["Image", "Mask"])
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))

    #     if len(files) > 1:
    #
    #         # start by selecting a pair of mask an img.
    #         img_path = os.path.join(root, "CT.nii")
    #
    #         # collect all masks in an array.
    #         mask_list = [f for f in files if "lesion" in f]
    #
    #         # iterate over an mask
    #         for m in mask_list:
    #             mask_path = os.path.join(root, m)
    #
    #             # write in dataframe.
    #             data = {"Image":[img_path], "Mask":[mask_path]}
    #             df_tmp = pd.DataFrame(data=data)
    #             df = df.append(df_tmp, ignore_index=True)
    #
    #
    # df.to_csv("files_loc.csv")


if __name__ == '__main__':
    main()

