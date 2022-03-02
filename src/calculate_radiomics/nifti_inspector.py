import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from batchviewer import view_batch


def images(img, mask):
    mask[mask > 1] = 1
    # mask[mask == 2] = 125
    print(np.unique(mask))
    plt.imshow(img, cmap="gray")
    plt.imshow(mask, alpha=0.3, cmap="jet")
    plt.show()

if __name__ == '__main__':
    file_path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/n_n_AT/TP1_20211014/CT.nii"
    mask_path = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/n_n_AT/TP1_20211014/lesion1(lk_left_pelvis).nii.gz"

    img = nib.load(file_path)
    mask = nib.load(mask_path)
    print(img.shape)
    print(img.header["pixdim"][1:4])
    img = img.get_fdata()
    mask = mask.get_fdata()
    # img = img.transpose(2, 3, 0, 1)
    img = img.transpose(2, 0, 1)
    mask = mask.transpose(2, 0, 1)
    # plt.imshow(img[..., 40], cmap=plt.cm.gray)


    slice = 111
    images(img[slice], mask[slice])






    view_batch(img, mask, width=512, height=512)


