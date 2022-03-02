import nibabel as nib
import radiomics
#from radiomics import featuresextractor
import os
import SimpleITK as sitk
import six
from radiomics import glcm, glrlm, glszm, imageoperations, shape


def main():
    path_img = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/Images/noname_noname_EG/TP1_20211019/CT.nii"
    path_mask = "/home/mfmezger/data/AI_Clinic_Data/NORA_EXPORT/Images/noname_noname_EG/TP1_20211019/lesion3(right_sacral).nii.gz"
    #
    # img = nib.load(path_img)
    # mask = nib.load(path_mask)
    # img = img.get_fdata()
    # mask = mask.get_fdata()
    # img = img.transpose(2,0,1)
    # mask = mask.transpose(2,0,1)

    img = sitk.ReadImage(path_img)
    mask = sitk.ReadImage(path_mask)
    settings = {'binWidth': 25,
                'interpolator': sitk.sitkBSpline,
                'resampledPixelSpacing': None}


    firstOrderFeatures = radiomics.firstorder.RadiomicsFirstOrder(img, mask, **settings)

    firstOrderFeatures.enableAllFeatures()


    results = firstOrderFeatures.execute()

    for (key, val) in six.iteritems(results):
        print('  ', key, ':', val)

    #
    # Show Shape features
    #
    shapeFeatures = shape.RadiomicsShape(img, mask, **settings)
    shapeFeatures.enableAllFeatures()
    
    results = shapeFeatures.execute()

    print('Calculated Shape features: ')
    for (key, val) in six.iteritems(results):
      print('  ', key, ':', val)
    
    #
    # Show GLCM features
    #
    glcmFeatures = glcm.RadiomicsGLCM(img, mask, **settings)
    glcmFeatures.enableAllFeatures()
    
    results = glcmFeatures.execute()

    print('Calculated GLCM features: ')
    for (key, val) in six.iteritems(results):
      print('  ', key, ':', val)
    
    #
    # Show GLRLM features
    #
    glrlmFeatures = glrlm.RadiomicsGLRLM(img, mask, **settings)
    glrlmFeatures.enableAllFeatures()
    
    results = glrlmFeatures.execute()

    print('Calculated GLRLM features: ')
    for (key, val) in six.iteritems(results):
      print('  ', key, ':', val)
    
    #
    # Show GLSZM features
    #
    glszmFeatures = glszm.RadiomicsGLSZM(img, mask, **settings)
    glszmFeatures.enableAllFeatures()
    
    results = glszmFeatures.execute()

    print('Calculated GLSZM features: ')
    for (key, val) in six.iteritems(results):
      print('  ', key, ':', val)
    




if __name__ == '__main__':
    main()
