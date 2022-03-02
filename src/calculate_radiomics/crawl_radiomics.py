import os
import pandas as pd
from calc_utils import calc_radiomics


def main():

    path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/"

    df = pd.DataFrame()
    for root, dirs, files in os.walk(path, topdown=True):
        # for name in files:
        #     print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))

        if len(files) > 1:

            # start by selecting a pair of mask an img.
            img_path = os.path.join(root, "CT.nii")

            # collect all masks in an array.
            mask_list = [f for f in files if "lesion" in f]

            # iterate over an mask
            for m in mask_list:
                mask_path = os.path.join(root, m)
                # todo : eventuell alles in einem?
                results_First_order, results_shape, results_glcm, results_glrlm, results_glszm = calc_radiomics(img_path, mask_path)

                res = pd.Series(results_First_order)

                # add patient identifier
                # todo id as index or  column name. id needs
                name = str(root.split("_")[-2].split("/")[0])
                number = mask_list.index(m)
                name += str(number)

                identifier = pd.Series([ name] )
                res = pd.concat(identifier[-1:], res)
                df = df.append(res, ignore_index=True)
                print()


if __name__ == '__main__':
    main()

